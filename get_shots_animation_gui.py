import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QCheckBox, QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTabWidget,
                               QVBoxLayout, QWidget)
from shiboken2 import wrapInstance

scriptpath = r"V:\Scripts"
sys.path.append(os.path.abspath(scriptpath))
import getShots
reload(getShots)

import maya.OpenMayaUI as apiUI


class FinalAnimWidget(QWidget):
    def __init__(self, parent=None):
        super(FinalAnimWidget, self).__init__(parent)

        self.btn_execute = None
        self.chk_bx_cache_anim = None
        self.chk_bx_cache_camera = None
        self.chk_bx_playblast_abc = None
        self.chk_bx_playblast_anim = None
        self.l_edit_description = None
        self.l_edit_shot_name = None

        self.setup_ui()
        self.setup_connections()

    def execute(self):
        getShots.finalAnim(
            shot_name=self.l_edit_shot_name.text(),
            description=self.l_edit_description.text(),
            playblast_anim=self.chk_bx_playblast_anim.checkState() is Qt.Checked,
            cache_anim=self.chk_bx_cache_anim.checkState() is Qt.Checked,
            cache_camera=self.chk_bx_cache_camera.checkState() is Qt.Checked,
            playblast_abc=self.chk_bx_playblast_abc.checkState() is Qt.Checked
        )

    def setup_connections(self):
        self.btn_execute.released.connect(self.execute)

    def setup_ui(self):
        lyt_v_main = QVBoxLayout()

        # Shot Name
        lyt_h_shot_name = QHBoxLayout()
        label_shot_name = QLabel("Shot Name")
        label_shot_name.setFixedWidth(100)
        label_shot_name.setAlignment(Qt.AlignRight)
        self.l_edit_shot_name = QLineEdit()
        lyt_h_shot_name.addWidget(label_shot_name)
        lyt_h_shot_name.addWidget(self.l_edit_shot_name)
        lyt_v_main.addLayout(lyt_h_shot_name)

        # Description
        lyt_h_description = QHBoxLayout()
        label_description = QLabel("Description")
        label_description.setFixedWidth(100)
        label_description.setAlignment(Qt.AlignRight)
        self.l_edit_description = QLineEdit()
        lyt_h_description.addWidget(label_description)
        lyt_h_description.addWidget(self.l_edit_description)
        lyt_v_main.addLayout(lyt_h_description)

        # Playblast Anim
        lyt_h_playblast_anim = QHBoxLayout()
        label_playblast_anim = QLabel("Playblast Anim")
        label_playblast_anim.setFixedWidth(100)
        label_playblast_anim.setAlignment(Qt.AlignRight)
        self.chk_bx_playblast_anim = QCheckBox()
        self.chk_bx_playblast_anim.setCheckState(Qt.Checked)
        lyt_h_playblast_anim.addWidget(label_playblast_anim)
        lyt_h_playblast_anim.addWidget(self.chk_bx_playblast_anim)
        lyt_h_playblast_anim.addStretch()
        lyt_v_main.addLayout(lyt_h_playblast_anim)

        # Cache Anim
        lyt_h_cache_anim = QHBoxLayout()
        label_cache_anim = QLabel("Cache Anim")
        label_cache_anim.setFixedWidth(100)
        label_cache_anim.setAlignment(Qt.AlignRight)
        self.chk_bx_cache_anim = QCheckBox()
        self.chk_bx_cache_anim.setCheckState(Qt.Checked)
        lyt_h_cache_anim.addWidget(label_cache_anim)
        lyt_h_cache_anim.addWidget(self.chk_bx_cache_anim)
        lyt_h_cache_anim.addStretch()
        lyt_v_main.addLayout(lyt_h_cache_anim)

        # Cache Camera
        lyt_h_cache_camera = QHBoxLayout()
        label_cache_camera = QLabel("Cache Camera")
        label_cache_camera.setFixedWidth(100)
        label_cache_camera.setAlignment(Qt.AlignRight)
        self.chk_bx_cache_camera = QCheckBox()
        self.chk_bx_cache_camera.setCheckState(Qt.Checked)
        lyt_h_cache_camera.addWidget(label_cache_camera)
        lyt_h_cache_camera.addWidget(self.chk_bx_cache_camera)
        lyt_h_cache_camera.addStretch()
        lyt_v_main.addLayout(lyt_h_cache_camera)

        # Playblast ABC
        lyt_h_playblast_abc = QHBoxLayout()
        label_playblast_abc = QLabel("Playblast ABC")
        label_playblast_abc.setFixedWidth(100)
        label_playblast_abc.setAlignment(Qt.AlignRight)
        self.chk_bx_playblast_abc = QCheckBox()
        self.chk_bx_playblast_abc.setCheckState(Qt.Checked)
        lyt_h_playblast_abc.addWidget(label_playblast_abc)
        lyt_h_playblast_abc.addWidget(self.chk_bx_playblast_abc)
        lyt_h_playblast_abc.addStretch()
        lyt_v_main.addLayout(lyt_h_playblast_abc)

        # Button
        self.btn_execute = QPushButton("Execute")
        lyt_v_main.addWidget(self.btn_execute)
        
        self.setLayout(lyt_v_main)


class GetShotInfoWidget(QWidget):
    def __init__(self, parent=None):
        super(GetShotInfoWidget, self).__init__(parent)

        self.btn_execute = None

        self.setup_ui()
        self.setup_connections()

    def setup_connections(self):
        self.btn_execute.released.connect(getShots.getShotInfo)

    def setup_ui(self):
        lyt_v_main = QVBoxLayout()

        # Button
        self.btn_execute = QPushButton("Execute")
        lyt_v_main.addWidget(self.btn_execute)

        self.setLayout(lyt_v_main)


class SetShotInfoWidget(QWidget):
    def __init__(self, parent=None):
        super(SetShotInfoWidget, self).__init__(parent)

        self.btn_execute = None
        self.l_edit_shot_name = None
        self.l_edit_shot_type = None
        self.l_edit_task_name = None

        self.setup_ui()
        self.setup_connections()

    def execute(self):
        getShots.setShotInfo(
            shot_name=self.l_edit_shot_name.text() if self.l_edit_shot_name.text() else None,
            shot_type=self.l_edit_shot_type.text() if self.l_edit_shot_type.text() else None,
            task_name=self.l_edit_task_name.text() if self.l_edit_task_name.text() else None
        )

    def setup_connections(self):
        self.btn_execute.released.connect(self.execute)

    def setup_ui(self):
        lyt_v_main = QVBoxLayout()

        # Shot Names
        lyt_h_shot_name = QHBoxLayout()
        label_shot_name = QLabel("Shot Name")
        label_shot_name.setFixedWidth(100)
        label_shot_name.setAlignment(Qt.AlignRight)
        self.l_edit_shot_name = QLineEdit()
        lyt_h_shot_name.addWidget(label_shot_name)
        lyt_h_shot_name.addWidget(self.l_edit_shot_name)
        lyt_v_main.addLayout(lyt_h_shot_name)

        # Shot Type
        lyt_h_shot_type = QHBoxLayout()
        label_shot_type = QLabel("Shot Type")
        label_shot_type.setFixedWidth(100)
        label_shot_type.setAlignment(Qt.AlignRight)
        self.l_edit_shot_type = QLineEdit()
        lyt_h_shot_type.addWidget(label_shot_type)
        lyt_h_shot_type.addWidget(self.l_edit_shot_type)
        lyt_v_main.addLayout(lyt_h_shot_type)

        # Task Name
        lyt_h_task_name = QHBoxLayout()
        label_task_name = QLabel("Task Name")
        label_task_name.setFixedWidth(100)
        label_task_name.setAlignment(Qt.AlignRight)
        self.l_edit_task_name = QLineEdit()
        lyt_h_task_name.addWidget(label_task_name)
        lyt_h_task_name.addWidget(self.l_edit_task_name)
        lyt_v_main.addLayout(lyt_h_task_name)

        # Button
        self.btn_execute = QPushButton("Execute")
        lyt_v_main.addWidget(self.btn_execute)
        
        self.setLayout(lyt_v_main)


class StartAnimWidget(QWidget):
    def __init__(self, parent=None):
        super(StartAnimWidget, self).__init__(parent)

        self.btn_execute = None
        self.chk_bx_download_assets = None
        self.chk_bx_download_previs = None
        self.chk_bx_ref_assets = None
        self.chk_bx_ref_previs = None
        self.chk_bx_start = None
        self.chk_bx_upload = None
        self.l_edit_shot_names = None
        self.l_edit_shot_type = None

        self.setup_ui()
        self.setup_connections()

    def execute(self):
        config = dict(
            shot_type=self.l_edit_shot_type.text(),  # type of scene
            shot_names=[s.strip() for s in self.l_edit_shot_names.text().split(",")] if self.l_edit_shot_names.text() else [],  # shots to build

            download_assets=self.chk_bx_download_assets.checkState() is Qt.Checked,  # check-out and save assets
            download_previs=self.chk_bx_download_previs.checkState() is Qt.Checked,  # check-out previs

            start=self.chk_bx_start.checkState() is Qt.Checked,  # start a new scene
            ref_assets=self.chk_bx_ref_assets.checkState() is Qt.Checked,  # reference assets into your scene
            ref_previs=self.chk_bx_ref_previs.checkState() is Qt.Checked,  # reference previs into your scene
            upload=self.chk_bx_upload.checkState() is Qt.Checked,  # check-in the shot
        )
        getShots.Scene(config=config).build()

    def setup_connections(self):
        self.btn_execute.released.connect(self.execute)

    def setup_ui(self):
        """

        """
        lyt_v_main = QVBoxLayout()

        # Shot type
        lyt_h_shot_type = QHBoxLayout()
        label_shot_type = QLabel("Shot Type")
        label_shot_type.setFixedWidth(100)
        label_shot_type.setAlignment(Qt.AlignRight)
        self.l_edit_shot_type = QLineEdit()
        lyt_h_shot_type.addWidget(label_shot_type)
        lyt_h_shot_type.addWidget(self.l_edit_shot_type)
        lyt_v_main.addLayout(lyt_h_shot_type)

        # Shot Names
        lyt_h_shot_names = QHBoxLayout()
        label_shot_names = QLabel("Shot Names")
        label_shot_names.setFixedWidth(100)
        label_shot_names.setAlignment(Qt.AlignRight)
        self.l_edit_shot_names = QLineEdit()
        lyt_h_shot_names.addWidget(label_shot_names)
        lyt_h_shot_names.addWidget(self.l_edit_shot_names)
        lyt_v_main.addLayout(lyt_h_shot_names)

        # Download Assets
        lyt_h_download_assets = QHBoxLayout()
        label_download_assets = QLabel("Download Assets")
        label_download_assets.setFixedWidth(100)
        label_download_assets.setAlignment(Qt.AlignRight)
        self.chk_bx_download_assets = QCheckBox()
        self.chk_bx_download_assets.setCheckState(Qt.Checked)
        lyt_h_download_assets.addWidget(label_download_assets)
        lyt_h_download_assets.addWidget(self.chk_bx_download_assets)
        lyt_h_download_assets.addStretch()
        lyt_v_main.addLayout(lyt_h_download_assets)

        # Download Previs
        lyt_h_download_previs = QHBoxLayout()
        label_download_previs = QLabel("Download Previs")
        label_download_previs.setFixedWidth(100)
        label_download_previs.setAlignment(Qt.AlignRight)
        self.chk_bx_download_previs = QCheckBox()
        self.chk_bx_download_previs.setCheckState(Qt.Checked)
        lyt_h_download_previs.addWidget(label_download_previs)
        lyt_h_download_previs.addWidget(self.chk_bx_download_previs)
        lyt_h_download_previs.addStretch()
        lyt_v_main.addLayout(lyt_h_download_previs)

        # Start
        lyt_h_start = QHBoxLayout()
        label_start = QLabel("Start")
        label_start.setFixedWidth(100)
        label_start.setAlignment(Qt.AlignRight)
        self.chk_bx_start = QCheckBox()
        self.chk_bx_start.setCheckState(Qt.Checked)
        lyt_h_start.addWidget(label_start)
        lyt_h_start.addWidget(self.chk_bx_start)
        lyt_h_start.addStretch()
        lyt_v_main.addLayout(lyt_h_start)

        # Reference Assets
        lyt_h_ref_assets = QHBoxLayout()
        label_ref_assets = QLabel("Reference Assets")
        label_ref_assets.setFixedWidth(100)
        label_ref_assets.setAlignment(Qt.AlignRight)
        self.chk_bx_ref_assets = QCheckBox()
        self.chk_bx_ref_assets.setCheckState(Qt.Checked)
        lyt_h_ref_assets.addWidget(label_ref_assets)
        lyt_h_ref_assets.addWidget(self.chk_bx_ref_assets)
        lyt_h_ref_assets.addStretch()
        lyt_v_main.addLayout(lyt_h_ref_assets)

        # Reference Previs
        lyt_h_ref_previs = QHBoxLayout()
        label_ref_previs = QLabel("Reference Previs")
        label_ref_previs.setFixedWidth(100)
        label_ref_previs.setAlignment(Qt.AlignRight)
        self.chk_bx_ref_previs = QCheckBox()
        self.chk_bx_ref_previs.setCheckState(Qt.Checked)
        lyt_h_ref_previs.addWidget(label_ref_previs)
        lyt_h_ref_previs.addWidget(self.chk_bx_ref_previs)
        lyt_h_ref_previs.addStretch()
        lyt_v_main.addLayout(lyt_h_ref_previs)

        # Upload
        lyt_h_upload = QHBoxLayout()
        label_upload = QLabel("Upload")
        label_upload.setFixedWidth(100)
        label_upload.setAlignment(Qt.AlignRight)
        self.chk_bx_upload = QCheckBox()
        self.chk_bx_upload.setCheckState(Qt.Checked)
        lyt_h_upload.addWidget(label_upload)
        lyt_h_upload.addWidget(self.chk_bx_upload)
        lyt_h_upload.addStretch()
        lyt_v_main.addLayout(lyt_h_upload)

        # Button
        self.btn_execute = QPushButton("Execute")
        lyt_v_main.addWidget(self.btn_execute)
        
        self.setLayout(lyt_v_main)


class TabsWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabsWidget, self).__init__(parent)

        self.addTab(StartAnimWidget(), "Start Anim")
        self.addTab(FinalAnimWidget(), "Final Anim")
        self.addTab(GetShotInfoWidget(), "Get Shot Info")
        self.addTab(SetShotInfoWidget(), "Set Shot Info")


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
    dialog.setWindowTitle("getShots - Animation")
    tabs_widget = TabsWidget(dialog)
    lyt_v_dialog = QVBoxLayout()
    lyt_v_dialog.addWidget(tabs_widget)
    dialog.setLayout(lyt_v_dialog)
    dialog.resize(500, dialog.size().height())

    dialog.show()
    