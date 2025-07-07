from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QCheckBox, QLineEdit, QPushButton, QLabel, QHBoxLayout
from qgis.core import QgsProject, QgsPointXY, QgsLineString, QgsVectorLayer, QgsFeature, QgsGeometry
from qgis.gui import QgsMapToolEmitPoint
from qgis.utils import iface
import math

class SpiralGeneratorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radial Line Generator")
        self.center_point = None
        
        # UI Elements
        layout = QVBoxLayout()
        
        self.group_name = QLineEdit("RadialGroup1")
        self.center_label = QLabel("Click map to set center")
        self.pick_center_btn = QPushButton("Pick Center")
        self.pick_center_btn.clicked.connect(self.set_map_tool)
        
        # Distance input
        self.distance_label = QLabel("Line Length (degrees):")
        self.distance_input = QLineEdit("10.0")

        # bearing inputs
        self.bearing_label_cw = QLabel("CW Bearing (degrees):")
        self.bearing_input_cw = QLineEdit("36.0")  # Default bearing for radial

        self.bearing_label_ccw = QLabel("CCW Bearing (degrees):")
        self.bearing_input_ccw = QLineEdit("36.0")
        
        # CW/CCW checkboxes
        cw_group = QGroupBox("CW Lines")
        ccw_group = QGroupBox("CCW Lines")
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
        
        # Buttons
        self.apply_btn = QPushButton("Generate Radial Lines")
        self.apply_btn.clicked.connect(self.generate_lines)
        
        # Assemble UI
        layout.addWidget(QLabel("Group Name:"))
        layout.addWidget(self.group_name)
        layout.addWidget(self.center_label)
        layout.addWidget(self.pick_center_btn)
        layout.addWidget(self.distance_label)
        layout.addWidget(self.distance_input)
        layout.addWidget(self.bearing_label_cw)
        layout.addWidget(self.bearing_input_cw)
        layout.addWidget(self.bearing_label_ccw)
        layout.addWidget(self.bearing_input_ccw)
        layout.addWidget(cw_group)
        layout.addWidget(ccw_group)
        layout.addWidget(self.apply_btn)
        
        self.setLayout(layout)

    def set_map_tool(self):
        self.map_tool = QgsMapToolEmitPoint(iface.mapCanvas())
        self.map_tool.canvasClicked.connect(self.set_center)
        iface.mapCanvas().setMapTool(self.map_tool)

    def set_center(self, point):
        self.center_point = point
        self.center_label.setText(f"Center: {point.x():.5f}, {point.y():.5f}")

    def generate_lines(self):
        if not self.center_point:
            iface.messageBar().pushWarning("Missing Center", "Please select a center point first")
            return
            
        try:
            distance = float(self.distance_input.text())
        except ValueError:
            iface.messageBar().pushWarning("Invalid Distance", "Please enter a valid number for distance")
            return
        
        try:
            bearing_cw = float(self.bearing_input_cw.text())
        except ValueError:
            iface.messageBar().pushWarning("Invalid bearing", "Please enter a valid number for CW bearing")
            return     

        try:
            bearing_ccw = float(self.bearing_input_ccw.text())
        except ValueError:
            iface.messageBar().pushWarning("Invalid bearing", "Please enter a valid number for CCW bearing")
            return
        
        group_name = self.group_name.text()
        project = QgsProject.instance()

        
        # Create layer groups
        root = project.layerTreeRoot()
        main_group = root.addGroup(group_name)
        cw_group = main_group.addGroup("cw")
        ccw_group = main_group.addGroup("ccw")
        
        # Generate radial lines (36° intervals)
        for i, cb in enumerate(self.cw_checks):
            if cb.isChecked():
                bearing = i * float(bearing_cw)  # CW bearing_cw  # Degrees
                layer = self.create_radial_layer(group_name, "cw", i+1, bearing, distance)
                project.addMapLayer(layer, False)
                cw_group.addLayer(layer)
                
        for i, cb in enumerate(self.ccw_checks):
            if cb.isChecked():
                bearing = -i * float(bearing_ccw)  # CCW bearing_ccw
                layer = self.create_radial_layer(group_name, "ccw", i+1, bearing, distance)
                project.addMapLayer(layer, False)
                ccw_group.addLayer(layer)
                
        iface.messageBar().pushSuccess("Success", f"Created radial lines for {group_name}")

    def create_radial_layer(self, group, direction, index, bearing, distance):
        """Create actual radial line layer"""
        layer_name = f"{group}_{direction}_{index}"
        layer = QgsVectorLayer("LineString?crs=EPSG:4326", layer_name, "memory")
        
        # Convert bearing to radians
        bearing_rad = math.radians(bearing)
        
        # Calculate endpoint
        end_x = self.center_point.x() + distance * math.cos(bearing_rad)
        end_y = self.center_point.y() + distance * math.sin(bearing_rad)
        
        # Create line feature
        line = QgsLineString([
            QgsPointXY(self.center_point.x(), self.center_point.y()),
            QgsPointXY(end_x, end_y)
        ])
        
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry(line))
        layer.dataProvider().addFeatures([feature])
        layer.updateExtents()
        return layer


# Create and show the dialog
dialog = SpiralGeneratorDialog()
dialog.show()