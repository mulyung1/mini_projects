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
dir = os.getcwd()  # Current working directory
csv_path = os.path.join(dir, 'Rangeland_Somalia_BRCiSIII.csv')
geometry_column = 'plot_details-polygon'      # Name of the column containing geometry data
crs = 'EPSG:4326'                   # Coordinate reference system (WGS84)

# Columns to add from CSV to the layer's attribute table
additional_columns = [
    "basic_info-name",
    "basic_info-date",
    "basic_info-organisation_name",
    "basic_info-organisation_other",
    "geography-state_name",
    "geography-region_name",
    "geography-district_name",
    "geography-community_name"
]

# Initialize the message bar
message_bar = iface.messageBar()     
message_bar.clearWidgets()           

try:
    if not csv_path or not geometry_column:
        message_bar.pushCritical("Input Error", "Missing CSV path or geometry column name")
        exit()

    # Create temporary polygon layer
    layer = QgsVectorLayer(f'Polygon?crs={crs}', 'polygons', 'memory')
    provider = layer.dataProvider()
    
    # Define layer fields structure
    fields = QgsFields()
    fields.append(QgsField('id', QVariant.Int))           
    fields.append(QgsField('area_m2', QVariant.Double))   
    fields.append(QgsField('area_unit', QVariant.String))
    # Add additional columns as String type
    for col in additional_columns:
        fields.append(QgsField(col, QVariant.String))
    provider.addAttributes(fields)
    layer.updateFields()

    da = QgsDistanceArea()
    da.setSourceCrs(layer.sourceCrs(), QgsProject.instance().transformContext())
    da.setEllipsoid('WGS84')

    row_count = 0 
    
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        
        # Check if required columns are present in CSV
        required_columns = [geometry_column] + additional_columns
        missing_columns = [col for col in required_columns if col not in reader.fieldnames]
        if missing_columns:
            message_bar.pushCritical("Input Error", f"Missing columns in CSV: {', '.join(missing_columns)}")
            exit()
        
        for row_id, row in enumerate(reader):
            try:
                geom_string = row[geometry_column]
                points = []
                valid = True

                for point_str in geom_string.split(';'):
                    components = point_str.strip().split()
                    if len(components) < 2:
                        valid = False
                        break
                    try:
                        lat, lon = float(components[0]), float(components[1])
                        points.append(QgsPointXY(lon, lat))
                    except ValueError:
                        valid = False
                        break

                if not valid or len(points) < 3:
                    if not valid:
                        message_bar.pushWarning("Data Warning", f"Row {row_id+1}: Invalid coordinates")
                    else:
                        message_bar.pushWarning("Geometry Error", f"Row {row_id+1}: Not enough points")
                    continue

                polygon = QgsGeometry.fromPolygonXY([points])  
                area = da.measureArea(polygon)  
                unit = QgsUnitTypes.toString(da.areaUnits())

                # Prepare attributes including additional columns
                attributes = [row_id, round(area, 4), unit]
                attributes += [row[col] for col in additional_columns]

                feat = QgsFeature()
                feat.setGeometry(polygon)
                feat.setAttributes(attributes)
                provider.addFeature(feat)
                row_count += 1

            except Exception as e:
                message_bar.pushCritical("Processing Error", f"Row {row_id+1}: {str(e)}")
                continue

    layer.updateExtents()
    QgsProject.instance().addMapLayer(layer)
    
    if row_count > 0:
        message_bar.pushSuccess("Complete", f"Added {row_count} valid polygons")
    else:
        message_bar.pushWarning("Result", "No valid polygons created")

except FileNotFoundError:
    message_bar.pushCritical("File Error", f"Missing CSV file: {csv_path}")
except Exception as e:
    message_bar.pushCritical("Runtime Error", f"Unexpected error: {str(e)}")