import math
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsLineString
from qgis.PyQt.QtCore import QVariant
from pyproj import Geod

geod = Geod(ellps="WGS84")

class SpiralGenerator:
    def __init__(self):
        self.params = {
            'spiral_stepping': 400,
            'spiral_ratio': 0.618,
            'density': 0.01,
            'cut_off_points': 0.03,
            'min_point_distance': 0.09
        }

    def get_antipode(self, lon, lat):
        """
        Returns the antipodal point (latitude, longitude) for given latitude and longitude.
        Inputs/outputs are in decimal degrees.
        """
        lat_a = -lat
        if lon <= 0:
            lon_a = lon + 180
        else:
            lon_a = lon - 180

        # Normalize longitude to range [-180, +180]
        if lon_a > 180:
            lon_a -= 360
        elif lon_a < -180:
            lon_a += 360

        return lon_a, lat_a

    def generate_spiral_points(self, start_lon, start_lat, azimuth, is_cw):
        """Generate spiral points from start to antipode"""
        antipode_lon, antipode_lat = self.get_antipode(start_lon, start_lat)
        
        print(antipode_lon, antipode_lat)
        
        # Spiral parameters
        steps = int(self.params['spiral_stepping'])
        log_step = math.log(geod.inv(start_lon, start_lat, antipode_lon, antipode_lat)[2] / 1000)
        bearings = []
        distances = []
        
        # Generate spiral path
        for i in range(steps):
            t = i / float(steps)
            angle = (azimuth + 360 * 10 * t) % 360
            if not is_cw:
                angle = (360 - angle) % 360
            bearings.append(angle)
            distances.append(math.exp(t * log_step) * 1000)  # Exponential distance scaling
        
        # Create points along spiral
        points = [QgsPointXY(start_lon, start_lat)]
        for dist, bearing in zip(distances, bearings):
            lon, lat, _ = geod.fwd(start_lon, start_lat, bearing, dist)
            points.append(QgsPointXY(lon, lat))
            
            # Stop when reaching antipode vicinity
            if abs(lon - antipode_lon) < 0.1 and abs(lat - antipode_lat) < 0.1:
                break
                
        return QgsLineString(points)

    def create_spiral_layer(self, center_lon, center_lat):
        """Create QGIS layer with spiral lines"""
        # Create memory layer
        layer = QgsVectorLayer("LineString?crs=EPSG:4326", "Logarithmic Spirals", "memory")
        provider = layer.dataProvider()
        provider.addAttributes([QgsField("direction", QVariant.String)])
        layer.updateFields()
        
        # Generate spirals
        features = []
        for direction in ["Right", "Left"]:
            is_cw = (direction == "Right")
            for i in range(10):
                azimuth = i * 36  # 0°, 36°, 72°, ... 324°
                line = self.generate_spiral_points(center_lon, center_lat, azimuth, is_cw)
                
                feature = QgsFeature()
                feature.setGeometry(QgsGeometry(line))
                feature.setAttributes([f"{direction} {azimuth}°"])
                features.append(feature)
        
        # Add features to layer
        provider.addFeatures(features)
        QgsProject.instance().addMapLayer(layer)

# Example usage:

generator = SpiralGenerator()
    
# Set your starting coordinates here (e.g., New York City)
#start_longitude = -74.0060
#start_latitude = 40.7128

#start_longitude = -167.5806 
#start_latitude = -32.7749
    
generator.create_spiral_layer(start_longitude, start_latitude)