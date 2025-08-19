import math
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QCheckBox, QLineEdit, QPushButton, QLabel, QHBoxLayout
from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsLineString, QgsLayerTreeLayer
from qgis.PyQt.QtCore import QVariant
from qgis.gui import QgsMapToolEmitPoint
from qgis.utils import iface
from pyproj import Geod
from qgis import processing

geod = Geod(ellps="WGS84")

class SpiralGenerator(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spiral Generator")
        self.center_point = None
        self.last_used_group_name = None  # Track last created group
        
        """-----------------UI Elements-----------------"""
        layout = QVBoxLayout()
        
        self.group_name = QLineEdit("SpiralGroup1")
        self.center_label = QLabel("Click map to set center")
        self.pick_center_btn = QPushButton("Pick Center")
        self.pick_center_btn.clicked.connect(self.set_map_tool)
        
        #distance inputs
        self.distance_label = QLabel("Minimum Distance Between Points (km):")
        self.min_point_dist = QLineEdit("1.0")
        
        # Bearing inputs
        self.bearing_label_cw = QLabel("CW Bearing Step (degrees):")
        self.bearing_input_cw = QLineEdit("36.0")
        
        self.bearing_label_ccw = QLabel("CCW Bearing Step (degrees):")
        self.bearing_input_ccw = QLineEdit("36.0")
        
        # CW/CCW checkboxes
        cw_group = QGroupBox("CW Spirals")
        ccw_group = QGroupBox("CCW Spirals")
        cw_layout = QHBoxLayout()
        ccw_layout = QHBoxLayout()
        
        self.cw_checks = [QCheckBox(f"CW {i+1}") for i in range(10)]
        self.ccw_checks = [QCheckBox(f"CCW {i+1}") for i in range(10)]
        
        for cb in self.cw_checks:
            cb.setChecked(True)
            cw_layout.addWidget(cb)
        for cb in self.ccw_checks:
            cb.setChecked(True)
            ccw_layout.addWidget(cb)
            
        cw_group.setLayout(cw_layout)
        ccw_group.setLayout(ccw_layout)
        
        # Assemble UI
        layout.addWidget(QLabel("Group Name:"))
        layout.addWidget(self.group_name)
        layout.addWidget(self.center_label)
        layout.addWidget(self.pick_center_btn)
        layout.addWidget(self.distance_label)
        layout.addWidget(self.min_point_dist)
        layout.addWidget(self.bearing_label_cw)
        layout.addWidget(self.bearing_input_cw)
        layout.addWidget(self.bearing_label_ccw)
        layout.addWidget(self.bearing_input_ccw)
        layout.addWidget(cw_group)
        layout.addWidget(ccw_group)
        
        self.setLayout(layout)

        # Connect signals for automatic updates
        self.bearing_input_cw.textEdited.connect(self.update_spiral_lines)
        self.bearing_input_ccw.textEdited.connect(self.update_spiral_lines)
        self.group_name.textEdited.connect(self.update_spiral_lines)
        
        for cb in self.cw_checks + self.ccw_checks:
            cb.stateChanged.connect(self.update_spiral_lines)

        # Hardcoded spiral parameters
        self.params = {
            'spiral_stepping': 200,       # Number of spiral segments
            'spiral_ratio': 0.000318,     # Growth factor
            'density': 0.6,               # Point density along spiral
            'cut_off_points': 0.1       # Antipode proximity threshold (degrees)
            #'min_point_distance': 1       # Minimum distance between points (km)
        }

    def set_map_tool(self):
        self.map_tool = QgsMapToolEmitPoint(iface.mapCanvas())
        self.map_tool.canvasClicked.connect(self.set_center)
        iface.mapCanvas().setMapTool(self.map_tool)

    def set_center(self, point):
        self.center_point = point
        self.center_label.setText(f"Center: {point.x():.5f}, {point.y():.5f}")
        self.update_spiral_lines()

    def remove_group(self, group_name):
        """Remove existing group and its layers"""
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        
        group_node = root.findGroup(group_name)
        if not group_node:
            return
            
        # Collect all layers in the group
        layers_to_remove = []
        def collect_layers(node):
            if isinstance(node, QgsLayerTreeLayer):
                layers_to_remove.append(node.layer())
            for child in node.children():
                collect_layers(child)
                
        collect_layers(group_node)
        
        # Remove group from layer tree
        parent = group_node.parent()
        parent.removeChildNode(group_node)
        
        # Remove layers from project
        for layer in layers_to_remove:
            project.removeMapLayer(layer)

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
    
    def generate_spiral_points(self, start_lon, start_lat, min_point_distance, azimuth, is_cw):
        """Generate spiral points ending at antipode"""
        # Calculate antipode first
        antipode_lon, antipode_lat = self.get_antipode(start_lon, start_lat)
        
        # Calculate total distance to antipode
        _, _, total_dist_m = geod.inv(start_lon, start_lat, antipode_lon, antipode_lat)
        total_dist_km = total_dist_m / 1000
        
        # Calculate growth parameters
        growth_factor = math.log(1 / self.params['spiral_ratio'])
        rotations = 10 * self.params['density']  # Adjust rotations by density
        
        points = [QgsPointXY(start_lon, start_lat)]
        prev_lon, prev_lat = start_lon, start_lat
        min_dist_m = min_point_distance * 1000  # Convert to meters
        
        # Generate points until we reach antipode proximity
        for i in range(1, self.params['spiral_stepping']):
            t = i / self.params['spiral_stepping']
            
            # Calculate angle with rotation control
            angle = (azimuth + rotations * 360 * t) % 360
            if not is_cw:
                angle = (360 - angle) % 360
            
            # Exponential distance calculation
            dist_km = total_dist_km * (math.exp(t * growth_factor) - 1) / (math.exp(growth_factor) - 1)
            lon, lat, _ = geod.fwd(start_lon, start_lat, angle, dist_km * 1000)
            
            # Skip points closer than minimum distance
            _, _, dist_to_prev = geod.inv(prev_lon, prev_lat, lon, lat)
            if dist_to_prev < min_dist_m:
                continue
                
            points.append(QgsPointXY(lon, lat))
            prev_lon, prev_lat = lon, lat
            
            # Check if we're close to antipode
            if (abs(lon - antipode_lon) < self.params['cut_off_points'] and 
                abs(lat - antipode_lat) < self.params['cut_off_points']):
                break
        
        # Always add antipode as the final point
        points.append(QgsPointXY(antipode_lon, antipode_lat))
        
        return points
    def create_spiral_layer(self, group, direction, index, min_point_distance, azimuth, is_cw):
        """Create a single spiral line layer"""
        layer_name = f"{group}_{direction}_{index}"
        layer = QgsVectorLayer("LineString?crs=EPSG:4326", layer_name, "memory")
        provider = layer.dataProvider()
        provider.addAttributes([
            QgsField("direction", QVariant.String),
            QgsField("azimuth", QVariant.Double),
            QgsField("type", QVariant.String)
        ])
        layer.updateFields()
        
        # Generate spiral points
        points = self.generate_spiral_points(
            self.center_point.x(), 
            self.center_point.y(), 
            min_point_distance,
            azimuth, 
            is_cw
        )
        
        # Create line feature
        line = QgsLineString(points)
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry(line))
        feature.setAttributes([
            direction,
            azimuth,
            "cw" if is_cw else "ccw"
        ])
        
        provider.addFeatures([feature])
        layer.updateExtents()
        return layer

    def update_spiral_lines(self):
        """Update spiral lines automatically when parameters change"""
        if not self.center_point:
            return
            
        # Get bearing values from UI
        try:
            bearing_cw = float(self.bearing_input_cw.text())
            bearing_ccw = float(self.bearing_input_ccw.text())
            min_point_dist = float(self.min_point_dist.text())
        except ValueError:
            return
            
        # Clear previous group if exists
        current_group_name = self.group_name.text()
        if self.last_used_group_name:
            self.remove_group(self.last_used_group_name)
            
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        
        # Create new layer groups
        main_group = root.insertGroup(0, current_group_name)
        cw_group = main_group.addGroup("cw")
        ccw_group = main_group.addGroup("ccw")
        
        # Generate CW spirals
        for i, cb in enumerate(self.cw_checks):
            if cb.isChecked():
                azimuth = i * bearing_cw
                layer = self.create_spiral_layer(
                    current_group_name, 
                    "cw", 
                    i+1, 
                    min_point_dist,
                    azimuth, 
                    True  # is_cw
                )
                project.addMapLayer(layer, False)
                cw_group.addLayer(layer)
                
        # Generate CCW spirals
        for i, cb in enumerate(self.ccw_checks):
            if cb.isChecked():
                azimuth = i * bearing_ccw
                layer = self.create_spiral_layer(
                    current_group_name, 
                    "ccw", 
                    i+1, 
                    min_point_dist,
                    azimuth, 
                    False  # is_cw
                )
                project.addMapLayer(layer, False)
                ccw_group.addLayer(layer)
                
        # Refresh map and track group
        iface.mapCanvas().refreshAllLayers()
        self.last_used_group_name = current_group_name


# Create and show the dialog
generator = SpiralGenerator()
generator.show()