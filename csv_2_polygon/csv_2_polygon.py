# Import required modules
import csv
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsField,
    QgsFields,
    QgsDistanceArea,
    QgsUnitTypes
)
from qgis.PyQt.QtCore import QVariant

import os

# Configuration parameters
dir = os.getcwd()  
csv_path = os.path.join(dir, 'Rangeland_Somalia_BRCiSIII.csv')

geometry_column = 'Plot Polygon'      # Name of the column containing geometry data
crs = 'EPSG:4326'                   # Coordinate reference system (WGS84)

#initialise the message bar
message_bar = iface.messageBar()     
# Clear previous messages
message_bar.clearWidgets()           


try:
    # Check if the CSV path and geometry column are provided
    if not csv_path or not geometry_column:
        message_bar.pushCritical("Input Error", "Missing CSV path or geometry column name")
        exit()

    # Create temporary polygon layer
    layer = QgsVectorLayer(f'Polygon?crs={crs}', 'polygons', 'memory')
    provider = layer.dataProvider()
    
    # Define layer fields structure >> in attribute table
    fields = QgsFields()
    fields.append(QgsField('id', QVariant.Int))           
    fields.append(QgsField('area_m2', QVariant.Double))   
    fields.append(QgsField('area_unit', QVariant.String)) 
    provider.addAttributes(fields)
    layer.updateFields()


    # Configure area calculator >> a geodesic measurement tool that works 
    # with coordinates in degrees and results in meteres, no need for 
    # reprojection of corner coordinates to utm.
    da = QgsDistanceArea()
    da.setSourceCrs(layer.sourceCrs(), QgsProject.instance().transformContext())
    da.setEllipsoid('WGS84')  # Enable ellipsoidal area calculations

     # polygon counter
    row_count = 0 
    
    # Read CSV file and process each row
    with open(csv_path, 'r') as file:
        # Read the CSV file to a dictionary
        reader = csv.DictReader(file)
        
        #
        for row_id, row in enumerate(reader):
            try:
                geom_string = row[geometry_column]
                
                #initialise empty list of qgis points(QgsPointXY) for polygon creation
                points = []
                valid = True


                # Split multi-point string(geometry column) into 4 components:
                # latitude, longitude, height, accuracy
                # split by whitespace and get every 4 elements separated by a ';', 
                # these are the corner coordinates of the polygon
                for point_str in geom_string.split(';'):
                    components = point_str.strip().split()
                    
                    # Validate minimum coordinate components
                    if len(components) < 2:
                        valid = False
                        break

                    # catch invalid coordinates from components 0& 1 lat & lon by converting to float
                    try:
                        lat = float(components[0]) 
                        lon = float(components[1]) 
                        points.append(QgsPointXY(lon, lat))  # qgis X/Y order
                    #if float fails, tag the row as an exception and report 
                    except ValueError:
                        valid = False
                        break

                # check for any tagged rows.
                if not valid:
                    message_bar.pushWarning("Data Warning", f"Row {row_id+1}: Invalid coordinates")
                    continue
                    
                if len(points) < 3:  # Minimum for polygon (triangle)
                    message_bar.pushWarning("Geometry Error", f"Row {row_id+1}: Not enough points")
                    continue
                # Create polygon from (QgsPointXY) point list
                polygon = QgsGeometry.fromPolygonXY([points])  

                # Compute area
                # Note: QgsDistanceArea uses the CRS of the layer for calculations
                # and returns the area in square meters because the 
                # area is calculated on the WGS84 ellipsoid.
                area = da.measureArea(polygon)  
                unit = QgsUnitTypes.toString(da.areaUnits())  # Get unit description as a check

                # create a new feature and set its geometry and attributes
                feat = QgsFeature()
                feat.setGeometry(polygon)
                feat.setAttributes([row_id, round(area, 4), unit])  # Round to 4 decimals
                #add the feature to the layer
                provider.addFeature(feat)
                
                #next row
                row_count += 1

            except Exception as e:
                message_bar.pushCritical("Processing Error", f"Row {row_id+1}: {str(e)}")
                continue

    #update the layer with the new features
    layer.updateExtents()  # Refresh layer bounds
    QgsProject.instance().addMapLayer(layer)  # Add to QGIS project
    
    #final status report
    if row_count > 0:
        print(f"Sucess: Added {row_count} valid polygons")
        message_bar.pushSuccess("Complete", f"Added {row_count} valid polygons")
    else:
        message_bar.pushWarning("Result", "No valid polygons created")

# user error handling
except FileNotFoundError:
    message_bar.pushCritical("File Error", f"Missing CSV file: {csv_path}")
except Exception as e:
    message_bar.pushCritical("Runtime Error", f"Unexpected error: {str(e)}")