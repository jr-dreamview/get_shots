import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QCheckBox, QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox,
                               QVBoxLayout, QWidget)
from shiboken2 import wrapInstance

scriptpath = r"V:\Scripts"
sys.path.append(os.path.abspath(scriptpath))
import getShots
reload(getShots)

import maya.OpenMayaUI as apiUI


class SceneWidget(QWidget):
    def __init__(self, parent=None):
        super(SceneWidget, self).__init__(parent)
        
        self.chk_bx_verbose = None
        self.l_edit_shot_type = None
        self.l_edit_shot_names = None
        self.l_edit_render_preset = None
        self.l_edit_aov_preset = None

        self.chk_bx_download_assets = None  # checks-out and saves each asset linked to the scene
        self.chk_bx_start = None  # check-out and start to create the project
        self.chk_bx_ref_assets = None  # references the assets into the scene
        self.chk_bx_render_settings = None  # imports the render settings preset
        self.chk_bx_aov_settings = None  # imports the aovs preset

        self.chk_bx_silopass_n_test = None  # render a frame for each dpack locally
        self.chk_bx_silopass_n_render = None  # check-in-and-render a frame for each dpack on the farm
        self.spn_bx_x_res = None  # horizontal render resolution
        self.spn_bx_y_res = None  # vertical render resolution
        self.l_edit_description = None

        self.btn_execute = None

        self.setup_ui()
        self.setup_connections()
    
    def execute(self):
        config = dict(
            # verbose=self.chk_bx_verbose.checkState() is Qt.Checked,
            shot_type=self.l_edit_shot_type.text(),
            shot_names=([s.strip() for s in self.l_edit_shot_names.text().split(",")]
                        if self.l_edit_shot_names.text() else []),
            render_preset=self.l_edit_render_preset.text(),
            aov_preset=self.l_edit_aov_preset.text(),

            download_assets=self.chk_bx_download_assets.checkState() is Qt.Checked,
            start=self.chk_bx_start.checkState() is Qt.Checked,
            ref_assets=self.chk_bx_ref_assets.checkState() is Qt.Checked,
            render_settings=self.chk_bx_render_settings.checkState() is Qt.Checked,
            aov_settings=self.chk_bx_aov_settings.checkState() is Qt.Checked,

            silopass_n_test=self.chk_bx_silopass_n_test.checkState() is Qt.Checked,
            silopass_n_render=self.chk_bx_silopass_n_render.checkState() is Qt.Checked,
            x_res=self.spn_bx_x_res.value(),
            y_res=self.spn_bx_y_res.value(),
            description=self.l_edit_description.text(),
        )
        # DEBUG
        print("\nDEBUG\n")
        for k in ["verbose", "shot_type", "shot_names", "render_preset", "aov_preset", "download_assets", "start",
                  "ref_assets", "render_settings", "aov_settings", "silopass_n_test", "silopass_n_render", "x_res",
                  "y_res", "description"]:
            print("{}: {}".format(k, config.get(k)))
        # getShots.Scene(config=config).build()
        
    def setup_connections(self):
        self.btn_execute.released.connect(self.execute)
        
    def setup_ui(self):
        lyt_v_main = QVBoxLayout()

        # # Verbose
        # lyt_h_verbose = QHBoxLayout()
        # label_verbose = QLabel("Verbose")
        # label_verbose.setFixedWidth(100)
        # label_verbose.setAlignment(Qt.AlignRight)
        # lyt_h_verbose.addWidget(label_verbose)
        # self.chk_bx_verbose = QCheckBox(self)
        # lyt_h_verbose.addWidget(self.chk_bx_verbose)
        # lyt_h_verbose.addStretch()
        # lyt_v_main.addLayout(lyt_h_verbose)

        # Shot type
        lyt_h_shot_type = QHBoxLayout()
        label_shot_type = QLabel("Shot Type")
        label_shot_type.setFixedWidth(100)
        label_shot_type.setAlignment(Qt.AlignRight)
        lyt_h_shot_type.addWidget(label_shot_type)
        self.l_edit_shot_type = QLineEdit(self)
        lyt_h_shot_type.addWidget(self.l_edit_shot_type)
        lyt_v_main.addLayout(lyt_h_shot_type)

        # Shot Names
        lyt_h_shot_names = QHBoxLayout()
        label_shot_names = QLabel("Silo Scene Setup")
        label_shot_names.setFixedWidth(100)
        label_shot_names.setAlignment(Qt.AlignRight)
        lyt_h_shot_names.addWidget(label_shot_names)
        self.l_edit_shot_names = QLineEdit(self)
        lyt_h_shot_names.addWidget(self.l_edit_shot_names)
        lyt_v_main.addLayout(lyt_h_shot_names)

        # Render Preset
        lyt_h_render_preset = QHBoxLayout()
        label_render_preset = QLabel("Render Preset")
        label_render_preset.setFixedWidth(100)
        label_render_preset.setAlignment(Qt.AlignRight)
        lyt_h_render_preset.addWidget(label_render_preset)
        self.l_edit_render_preset = QLineEdit(self)
        lyt_h_render_preset.addWidget(self.l_edit_render_preset)
        lyt_v_main.addLayout(lyt_h_render_preset)

        # AOV Preset
        lyt_h_aov_preset = QHBoxLayout()
        label_aov_preset = QLabel("AOV Preset")
        label_aov_preset.setFixedWidth(100)
        label_aov_preset.setAlignment(Qt.AlignRight)
        lyt_h_aov_preset.addWidget(label_aov_preset)
        self.l_edit_aov_preset = QLineEdit(self)
        lyt_h_aov_preset.addWidget(self.l_edit_aov_preset)
        lyt_v_main.addLayout(lyt_h_aov_preset)

        # X Resolution
        lyt_h_x_res = QHBoxLayout()
        label_x_res = QLabel("X Resolution")
        label_x_res.setFixedWidth(100)
        label_x_res.setAlignment(Qt.AlignRight)
        lyt_h_x_res.addWidget(label_x_res)
        self.spn_bx_x_res = QSpinBox(self)
        self.spn_bx_x_res.setMinimum(1)
        self.spn_bx_x_res.setMaximum(4000)
        self.spn_bx_x_res.setValue(1000)
        self.spn_bx_x_res.setSuffix("px")
        lyt_h_x_res.addWidget(self.spn_bx_x_res)
        lyt_h_x_res.addStretch()
        lyt_v_main.addLayout(lyt_h_x_res)

        # Y Resolution
        lyt_h_y_res = QHBoxLayout()
        label_y_res = QLabel("Y Resolution")
        label_y_res.setFixedWidth(100)
        label_y_res.setAlignment(Qt.AlignRight)
        lyt_h_y_res.addWidget(label_y_res)
        self.spn_bx_y_res = QSpinBox(self)
        self.spn_bx_y_res.setMinimum(1)
        self.spn_bx_y_res.setMaximum(4000)
        self.spn_bx_y_res.setValue(1000)
        self.spn_bx_y_res.setSuffix("px")
        lyt_h_y_res.addWidget(self.spn_bx_y_res)
        lyt_h_y_res.addStretch()
        lyt_v_main.addLayout(lyt_h_y_res)

        # Download Assets
        lyt_h_download_assets = QHBoxLayout()
        label_download_assets = QLabel("Download Assets")
        label_download_assets.setFixedWidth(100)
        label_download_assets.setAlignment(Qt.AlignRight)
        lyt_h_download_assets.addWidget(label_download_assets)
        self.chk_bx_download_assets = QCheckBox(self)
        self.chk_bx_download_assets.setCheckState(Qt.Checked)
        lyt_h_download_assets.addWidget(self.chk_bx_download_assets)
        lyt_h_download_assets.addStretch()
        lyt_v_main.addLayout(lyt_h_download_assets)

        # Start
        lyt_h_start = QHBoxLayout()
        label_start = QLabel("Build")
        label_start.setFixedWidth(100)
        label_start.setAlignment(Qt.AlignRight)
        lyt_h_start.addWidget(label_start)
        self.chk_bx_start = QCheckBox(self)
        self.chk_bx_start.setCheckState(Qt.Checked)
        lyt_h_start.addWidget(self.chk_bx_start)
        lyt_h_start.addStretch()
        lyt_v_main.addLayout(lyt_h_start)

        # Reference Assets
        lyt_h_ref_assets = QHBoxLayout()
        label_ref_assets = QLabel("Reference Assets")
        label_ref_assets.setFixedWidth(100)
        label_ref_assets.setAlignment(Qt.AlignRight)
        lyt_h_ref_assets.addWidget(label_ref_assets)
        self.chk_bx_ref_assets = QCheckBox(self)
        self.chk_bx_ref_assets.setCheckState(Qt.Checked)
        lyt_h_ref_assets.addWidget(self.chk_bx_ref_assets)
        lyt_h_ref_assets.addStretch()
        lyt_v_main.addLayout(lyt_h_ref_assets)

        # Render Settings
        lyt_h_render_settings = QHBoxLayout()
        label_render_settings = QLabel("Render Settings")
        label_render_settings.setFixedWidth(100)
        label_render_settings.setAlignment(Qt.AlignRight)
        lyt_h_render_settings.addWidget(label_render_settings)
        self.chk_bx_render_settings = QCheckBox(self)
        self.chk_bx_render_settings.setCheckState(Qt.Checked)
        lyt_h_render_settings.addWidget(self.chk_bx_render_settings)
        lyt_h_render_settings.addStretch()
        lyt_v_main.addLayout(lyt_h_render_settings)

        # AOV Settings
        lyt_h_aov_settings = QHBoxLayout()
        label_aov_settings = QLabel("AOV Settings")
        label_aov_settings.setFixedWidth(100)
        label_aov_settings.setAlignment(Qt.AlignRight)
        lyt_h_aov_settings.addWidget(label_aov_settings)
        self.chk_bx_aov_settings = QCheckBox(self)
        self.chk_bx_aov_settings.setCheckState(Qt.Checked)
        lyt_h_aov_settings.addWidget(self.chk_bx_aov_settings)
        lyt_h_aov_settings.addStretch()
        lyt_v_main.addLayout(lyt_h_aov_settings)

        # Silopass and Test
        lyt_h_silopass_n_test = QHBoxLayout()
        label_silopass_n_test = QLabel("Local Render")
        label_silopass_n_test.setFixedWidth(100)
        label_silopass_n_test.setAlignment(Qt.AlignRight)
        lyt_h_silopass_n_test.addWidget(label_silopass_n_test)
        self.chk_bx_silopass_n_test = QCheckBox(self)
        lyt_h_silopass_n_test.addWidget(self.chk_bx_silopass_n_test)
        lyt_h_silopass_n_test.addStretch()
        lyt_v_main.addLayout(lyt_h_silopass_n_test)

        # Silopass and Render
        lyt_h_silopass_n_render = QHBoxLayout()
        label_silopass_n_render = QLabel("Farm Render")
        label_silopass_n_render.setFixedWidth(100)
        label_silopass_n_render.setAlignment(Qt.AlignRight)
        lyt_h_silopass_n_render.addWidget(label_silopass_n_render)
        self.chk_bx_silopass_n_render = QCheckBox(self)
        lyt_h_silopass_n_render.addWidget(self.chk_bx_silopass_n_render)
        lyt_h_silopass_n_render.addStretch()
        lyt_v_main.addLayout(lyt_h_silopass_n_render)

        # Description
        lyt_h_description = QHBoxLayout()
        label_description = QLabel("Description")
        label_description.setFixedWidth(100)
        label_description.setAlignment(Qt.AlignRight)
        lyt_h_description.addWidget(label_description)
        self.l_edit_description = QLineEdit(self)
        lyt_h_description.addWidget(self.l_edit_description)
        lyt_v_main.addLayout(lyt_h_description)

        # Button
        self.btn_execute = QPushButton("Execute", self)
        lyt_v_main.addWidget(self.btn_execute)

        self.setLayout(lyt_v_main)


def get_maya_main_window():
    """Get the Maya main window.

    Returns:
        PySide2.QtWidgets.QWidget: 'MainWindow' Maya main window.
    """
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return wrapInstance(int(ptr), QWidget)


if __name__ == "__main__":
    dialog = QDialog(get_maya_main_window())
    dialog.setWindowTitle("SGK Silo")
    tabs_widget = SceneWidget(dialog)
    lyt_v_dialog = QVBoxLayout()
    lyt_v_dialog.addWidget(tabs_widget)
    dialog.setLayout(lyt_v_dialog)
    dialog.resize(500, dialog.size().height())

    dialog.show()
    