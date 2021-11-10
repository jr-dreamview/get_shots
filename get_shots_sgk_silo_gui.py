import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QComboBox, QDialog, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget)
from shiboken2 import wrapInstance

scriptpath = r"V:\Scripts"
sys.path.append(os.path.abspath(scriptpath))
import getShots
reload(getShots)

import maya.OpenMayaUI as apiUI


LABEL_WIDTH = 90
RES_DEFAULT = 1000
RES_MAX = 8192


class SceneWidget(QWidget):
    def __init__(self, parent=None):
        super(SceneWidget, self).__init__(parent)

        self.l_edit_shot_name = None
        self.l_edit_render_preset = None
        self.l_edit_aov_preset = None

        self.spn_bx_x_res = None  # horizontal render resolution
        self.spn_bx_y_res = None  # vertical render resolution
        self.l_edit_description = None

        self.btn_execute_build = None
        self.btn_update_button = None
        self.btn_reframing = None
        self.btn_execute_farm = None
        self.btn_execute_local = None
        self.btn_get_shot = None

        self.setup_ui()
        self.setup_connections()

    def execute_build(self):
        config = dict(
            verbose=False,
            shot_type="silosetup",
            shot_names=self.l_edit_shot_name.text(),
            render_preset=self.l_edit_render_preset.currentText(),
            aov_preset=self.l_edit_aov_preset.currentText(),

            download_assets=True,
            start=True,
            ref_assets=True,
            render_settings=bool(self.l_edit_render_preset.currentText()),
            aov_settings=bool(self.l_edit_aov_preset.currentText()),

            silopass_n_test=False,
            silopass_n_render=False,
            x_res=self.spn_bx_x_res.value(),
            y_res=self.spn_bx_y_res.value(),
            description=self.l_edit_description.text(),
        )
        self.print_config(config)
        # getShots.Scene(config=config).build()

    def execute_render_farm(self):
        config = dict(
            verbose=False,
            shot_type="silosetup",
            shot_names=self.l_edit_shot_name.text(),
            render_preset=self.l_edit_render_preset.currentText(),
            aov_preset=self.l_edit_aov_preset.currentText(),

            download_assets=False,
            start=False,
            ref_assets=False,
            render_settings=bool(self.l_edit_render_preset.currentText()),
            aov_settings=bool(self.l_edit_aov_preset.currentText()),

            silopass_n_test=False,
            silopass_n_render=True,
            x_res=self.spn_bx_x_res.value(),
            y_res=self.spn_bx_y_res.value(),
            description=self.l_edit_description.text(),
        )
        self.print_config(config)
        # getShots.Scene(config=config).build()

    def execute_render_local(self):
        config = dict(
            verbose=False,
            shot_type="silosetup",
            shot_names=self.l_edit_shot_name.text(),
            render_preset=self.l_edit_render_preset.currentText(),
            aov_preset=self.l_edit_aov_preset.currentText(),

            download_assets=False,
            start=False,
            ref_assets=False,
            render_settings=bool(self.l_edit_render_preset.currentText()),
            aov_settings=bool(self.l_edit_aov_preset.currentText()),

            silopass_n_test=True,
            silopass_n_render=False,
            x_res=self.spn_bx_x_res.value(),
            y_res=self.spn_bx_y_res.value(),
            description=self.l_edit_description.text(),
        )
        self.print_config(config)
        # getShots.Scene(config=config).build()

    @staticmethod
    def print_config(config):
        # DEBUG
        print("\nDEBUG\n")
        for k in ["verbose", "shot_type", "shot_names", "render_preset", "aov_preset", "download_assets", "start",
                  "ref_assets", "render_settings", "aov_settings", "silopass_n_test", "silopass_n_render", "x_res",
                  "y_res", "description"]:
            print("{}: {}".format(k, config.get(k)))

    def setup_connections(self):
        self.btn_execute_build.released.connect(self.execute_build)
        self.btn_execute_local.released.connect(self.execute_render_local)
        self.btn_execute_farm.released.connect(self.execute_render_farm)

    def setup_ui(self):
        lyt_v_main = QVBoxLayout()

        # Silo Scene Setup Group Box
        grp_bx_scene = QGroupBox(self)
        grp_bx_scene.setTitle("Silo Scene Setup")
        lyt_v_scene = QVBoxLayout()
        lyt_h_set_shot = QHBoxLayout()
        label_set_shot = QLabel("Set Shot", self)
        label_set_shot.setFixedWidth(LABEL_WIDTH)
        label_set_shot.setAlignment(Qt.AlignRight)
        lyt_h_set_shot.addWidget(label_set_shot)
        cmb_bx_set_shot = QComboBox(self)
        cmb_bx_set_shot.addItems(["", "Shot1", "Shot2", "Shot3"])
        lyt_h_set_shot.addWidget(cmb_bx_set_shot)
        lyt_v_scene.addLayout(lyt_h_set_shot)
        self.btn_get_shot = QPushButton("Get Shot", parent=self)
        lyt_v_scene.addWidget(self.btn_get_shot)
        lyt_h_shot_name = QHBoxLayout()
        label_shot_name = QLabel("Scene", self)
        label_shot_name.setFixedWidth(LABEL_WIDTH)
        label_shot_name.setAlignment(Qt.AlignRight)
        lyt_h_shot_name.addWidget(label_shot_name)
        self.l_edit_shot_name = QLineEdit(self)
        self.l_edit_shot_name.setEnabled(False)
        lyt_h_shot_name.addWidget(self.l_edit_shot_name)
        lyt_v_scene.addLayout(lyt_h_shot_name)
        grp_bx_scene.setLayout(lyt_v_scene)
        lyt_v_main.addWidget(grp_bx_scene)

        # Render Preset
        lyt_h_render_preset = QHBoxLayout()
        label_render_preset = QLabel("Render Preset")
        label_render_preset.setFixedWidth(LABEL_WIDTH)
        label_render_preset.setAlignment(Qt.AlignRight)
        lyt_h_render_preset.addWidget(label_render_preset)
        self.l_edit_render_preset = QComboBox(self)
        self.l_edit_render_preset.addItems(["", "Render Preset 1", "Render Preset 2"])
        lyt_h_render_preset.addWidget(self.l_edit_render_preset)
        lyt_v_main.addLayout(lyt_h_render_preset)

        # AOV Preset
        lyt_h_aov_preset = QHBoxLayout()
        label_aov_preset = QLabel("AOV Preset")
        label_aov_preset.setFixedWidth(LABEL_WIDTH)
        label_aov_preset.setAlignment(Qt.AlignRight)
        lyt_h_aov_preset.addWidget(label_aov_preset)
        self.l_edit_aov_preset = QComboBox(self)
        self.l_edit_aov_preset.addItems(["", "AOV Preset 1", "AOV Preset 2"])
        lyt_h_aov_preset.addWidget(self.l_edit_aov_preset)
        lyt_v_main.addLayout(lyt_h_aov_preset)

        # Resolution
        lyt_h_res = QHBoxLayout()
        label_res = QLabel("Resolution")
        label_res.setFixedWidth(LABEL_WIDTH)
        label_res.setAlignment(Qt.AlignRight)
        lyt_h_res.addWidget(label_res)
        label_x = QLabel("X:")
        lyt_h_res.addWidget(label_x)
        self.spn_bx_x_res = QSpinBox(self)
        self.spn_bx_x_res.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.spn_bx_x_res.setMinimum(1)
        self.spn_bx_x_res.setMaximum(RES_MAX)
        self.spn_bx_x_res.setValue(RES_DEFAULT)
        self.spn_bx_x_res.setSuffix("px")
        lyt_h_res.addWidget(self.spn_bx_x_res)
        label_y = QLabel("Y:")
        lyt_h_res.addWidget(label_y)
        self.spn_bx_y_res = QSpinBox(self)
        self.spn_bx_y_res.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.spn_bx_y_res.setMinimum(1)
        self.spn_bx_y_res.setMaximum(RES_MAX)
        self.spn_bx_y_res.setValue(RES_DEFAULT)
        self.spn_bx_y_res.setSuffix("px")
        lyt_h_res.addWidget(self.spn_bx_y_res)
        lyt_h_res.addStretch()
        lyt_v_main.addLayout(lyt_h_res)

        # Update Button
        lyt_h_buttons = QHBoxLayout()
        self.btn_execute_build = QPushButton("Build", self)
        lyt_h_buttons.addWidget(self.btn_execute_build)
        self.btn_update_button = QPushButton("Update", self)
        lyt_h_buttons.addWidget(self.btn_update_button)
        self.btn_reframing = QPushButton("Reframe", self)
        lyt_h_buttons.addWidget(self.btn_reframing)
        lyt_v_main.addLayout(lyt_h_buttons)

        # Description
        lyt_h_description = QHBoxLayout()
        label_description = QLabel("Description")
        label_description.setFixedWidth(LABEL_WIDTH)
        label_description.setAlignment(Qt.AlignRight)
        lyt_h_description.addWidget(label_description)
        self.l_edit_description = QLineEdit(self)
        lyt_h_description.addWidget(self.l_edit_description)
        lyt_v_main.addLayout(lyt_h_description)

        # Render Buttons
        lyt_h_render_buttons = QHBoxLayout()
        self.btn_execute_farm = QPushButton("Render - Farm", self)
        self.btn_execute_local = QPushButton("Render - Local", self)
        lyt_h_render_buttons.addWidget(self.btn_execute_farm)
        lyt_h_render_buttons.addWidget(self.btn_execute_local)
        lyt_v_main.addLayout(lyt_h_render_buttons)

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
    