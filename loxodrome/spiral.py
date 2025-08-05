import math
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsLineString
from qgis.PyQt.QtCore import QVariant
from pyproj import Geod

geod = Geod(ellps="WGS84")

class SpiralGenerator:
    def __init__(self):
        self.params = {
            'spiral_stepping': 200,       # Number of spiral segments
            'spiral_ratio': 0.618,         # Growth factor (Golden Ratio)
            'density': 0.1,                # Point density along spiral
            'cut_off_points': 0.5,         # Antipode proximity threshold (degrees)
            'min_point_distance': 0.9      # Minimum distance between points (km)
        }

    def get_antipode(self, lon, lat):
        """Calculate antipodal point with normalization"""
        lat_a = -lat
        lon_a = lon + 180 if lon <= 0 else lon - 180
        
        # Normalize longitude
        if lon_a > 180:
            lon_a -= 360
        elif lon_a < -180:
            lon_a += 360

        return lon_a, lat_a

    def generate_spiral_points(self, start_lon, start_lat, azimuth, is_cw):
        """Generate optimized spiral points with parameter controls"""
        antipode_lon, antipode_lat = self.get_antipode(start_lon, start_lat)
        
        # Calculate total distance to antipode
        _, _, total_dist_m = geod.inv(start_lon, start_lat, antipode_lon, antipode_lat)
        total_dist_km = total_dist_m / 1000
        
        # Calculate growth parameters
        growth_factor = math.log(1 / self.params['spiral_ratio'])
        rotations = 10 * self.params['density']  # Adjust rotations by density
        
        points = [QgsPointXY(start_lon, start_lat)]
        prev_lon, prev_lat = start_lon, start_lat
        min_dist_m = self.params['min_point_distance'] * 1000  # Convert to meters
        
        for i in range(1, self.params['spiral_stepping']):
            t = i / self.params['spiral_stepping']
            
            # Calculate angle with rotation control
            angle = (azimuth + rotations * 360 * t) % 360
            if not is_cw:
                angle = (360 - angle) % 360
            
            # Exponential distance calculation with growth factor
            dist_km = total_dist_km * (math.exp(t * growth_factor) - 1) / (math.exp(growth_factor) - 1)
            lon, lat, _ = geod.fwd(start_lon, start_lat, angle, dist_km * 1000)
            
            # Check antipode proximity
            if (abs(lon - antipode_lon) < self.params['cut_off_points'] and 
                abs(lat - antipode_lat) < self.params['cut_off_points']):
                break
                
            # Skip points closer than minimum distance
            _, _, dist_to_prev = geod.inv(prev_lon, prev_lat, lon, lat)
            if dist_to_prev < min_dist_m:
                continue
                
            points.append(QgsPointXY(lon, lat))
            prev_lon, prev_lat = lon, lat

        return QgsLineString(points)

    def create_spiral_layer(self, center_lon, center_lat):
        """Create spiral layer with optimized parameters"""
        layer = QgsVectorLayer("LineString?crs=EPSG:4326", "Optimized Spirals", "memory")
        provider = layer.dataProvider()
        provider.addAttributes([QgsField("direction", QVariant.String)])
        layer.updateFields()
        
        features = []
        for direction in ["Right", "Left"]:
            is_cw = (direction == "Right")
            for i in range(10):
                azimuth = i * 36
                line = self.generate_spiral_points(center_lon, center_lat, azimuth, is_cw)
                
                feature = QgsFeature()
                feature.setGeometry(QgsGeometry(line))
                feature.setAttributes([f"{direction} {azimuth}°"])
                features.append(feature)
        
        provider.addFeatures(features)
        QgsProject.instance().addMapLayer(layer)

# Example usage
generator = SpiralGenerator()
generator.create_spiral_layer(-74.0060, 40.7128)  # New York City coordinates