# -*- coding: utf-8 -*-


import sys

from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QSlider, QComboBox
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

import maya.cmds as cmds

from turntable_controller import TurntableController


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    Returns:
        class: QtWidget
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QWidget)


# Create a subclass of QMWidget to set up the TurnTable's GUI
class TurntableView(QWidget):
    """TurnTable View (GUI).
       Args:
           QWidget: Inherits properties from the QWidget module

       Attributes:
           turntable_view_instance(Class Type): Turntable UI window,
           It is set to none so we can check if this is the first
           instance of the Turntable UI window or if there is another
           instance running
    """

    turntable_view_instance = None

    @classmethod
    def show_turntable(cls):
        """Class method that will be used to run the tool in a production
           environment
        """
        if not cmds.ls(sl=True):
            cmds.error("Select an object")

        if cmds.ls("camera_render1"):
            cmds.warning("There is a camera_render1 and an offset created already, check your maya windows")
            cmds.delete("camera_render1", "offset_cameraRender1")
            cmds.select("pSphere1")
            cls.turntable_view_instance = TurntableView()
            cls.turntable_view_instance.main()
            cls.turntable_view_instance.close()
            cls.turntable_view_instance.deleteLater()

        elif not cls.turntable_view_instance:
            cls.turntable_view_instance = TurntableView()
            cls.turntable_view_instance.main()
            cls.turntable_view_instance.show()
            
        if cls.turntable_view_instance.isHidden():
            cls.turntable_view_instance.show()

        else:
            cls.turntable_view_instance.raise_()
            cls.turntable_view_instance.activateWindow()

    def __init__(self):
        """View initializer.
           Attributes:
                 general_layout: Set the general layout of the window
                 setWindowTitle: Set the window title
        """
        super(TurntableView, self).__init__()
        # Set some main window's properties
        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)

        # Set the window's title
        self.setWindowTitle('Turn Table')

        # Create the buttons
        self.create_display()
        self.camera_distance_section()
        self.camera_height_section()
        self.angle_interval_section_widgets()
        self.okay_and_cancel()

        # set the signals and slots for the buttons
        self.create_methods()

    def create_display(self):
        """This function creates a QLineEdit Widget that displays
           the name of the selected object
           Attributes:
               display_section_layout: Vertical layout
               name_label: Label displaying the title
               object_display: QLineEdit displaying the name of the selected object
        """

        # Set this section layout
        display_section_layout = QVBoxLayout()
        name_label = QLabel("Turn Table")
        # Add the widget to the layout
        display_section_layout.addWidget(name_label)
        # Add this section layout to the general layout
        self.general_layout.addLayout(display_section_layout)

        # Build the widget that displays the selected object name
        object_display = QLineEdit()
        object_display.setText(TurntableController.get_object_name())
        # Set display to read Only mode
        object_display.setReadOnly(True)
        # Add the widget to the layout
        display_section_layout.addWidget(object_display)
        # Add this section layout to the general layout
        self.general_layout.addLayout(display_section_layout)

    def camera_distance_section(self):
        """This function creates the widgets of the distance section
           A slide widget to control how close the camera will be from
           the selected object and a Qlabel widget above that slider that
           shows the info
           Attributes:
               distance_section_layout: Vertical layout
           """
        # Set the layout of this section
        distance_section_layout = QVBoxLayout()
        name_label = QLabel("Control the camera distance:")
        # Create the slider widget
        self.distance_slider = QSlider()
        # Set the slider to horizontal position
        self.distance_slider.setOrientation(Qt.Horizontal)
        # Setting the Ticks
        self.distance_slider.setTickPosition(QSlider.TicksBelow)
        self.distance_slider.setTickInterval(1)
        # Set the minimum value to 1 and maximum value to 10
        self.distance_slider.setMinimum(2)
        self.distance_slider.setMaximum(10)
        # Set the starting value to 5
        self.distance_slider.setValue(5)
        # Adding the widgets to the layout
        distance_section_layout.addWidget(name_label)
        distance_section_layout.addWidget(self.distance_slider)
        # Adding this section layout to the general layout
        self.general_layout.addLayout(distance_section_layout)

    def camera_height_section(self):
        """This function creates the widgets of the height section.
           A slides widget to control the height of the camera and a Qlabel
           widget above that slider that shows the info
        """

        # Set the layout of this section
        height_section_layout = QVBoxLayout()
        name_label = QLabel("Control the height of the camera :")
        # Create slider
        self.height_slider = QSlider()
        # Set the slider to horizontal position
        self.height_slider.setOrientation(Qt.Horizontal)
        # Set the ticks
        self.height_slider.setTickPosition(QSlider.TicksBelow)
        self.height_slider.setTickInterval(1)
        # Set the minimum value to -1 and maximum value to 20
        self.height_slider.setMinimum(-1)
        self.height_slider.setMaximum(10)
        # Set the starting value to 0
        self.height_slider.setValue(0)
        # Add the widgets to the layout
        height_section_layout.addWidget(name_label)
        height_section_layout.addWidget(self.height_slider)
        # Add this section layout to the general layout
        self.general_layout.addLayout(height_section_layout)

    def angle_interval_section_widgets(self):
        """Section where the interval value can be changed
           Two widgets are used, a combo box and a push button.
           A label is used to display the name of the
           section
        """
        # Define this section layout
        interval_angle_section_t_layout = QVBoxLayout()
        name_label = QLabel("Set the interval value")
        # Add the widget
        interval_angle_section_t_layout.addWidget(name_label)
        # Add this section to the general layout
        self.general_layout.addLayout(interval_angle_section_t_layout)

        # Create the combo box
        self.interval_angle_selector = QComboBox()
        # Adding the list of values to the Combo box
        self.interval_angle_selector.addItems(["2", "5", "10", "12", "25", "45", "180", "210"])
        # Adding the widgets
        interval_angle_section_t_layout.addWidget(self.interval_angle_selector)
        # Adding this section to the general layout
        self.general_layout.addLayout(interval_angle_section_t_layout)

    def create_methods(self):
        """This function creates some signals and slots
           to make the buttons work.
           The functions or actions the buttons are going to do
           are imported from the TurntableController script
        """
        self.distance_slider.valueChanged.connect(
            lambda: TurntableController.set_traslation(self.distance_slider.value()))
        self.height_slider.valueChanged.connect(lambda: TurntableController.set_height(self.height_slider.value()))

        self.interval_angle_selector.activated.connect(
            lambda: TurntableController.create_rotation(self.interval_angle_selector.currentText()))
        self.interval_angle_selector.highlighted.connect(TurntableController.delete_rotation)

        self.cancel_button.clicked.connect(lambda: TurntableController.cancel(self.close()))
        self.okay_button.clicked.connect(self.close)

    def okay_and_cancel(self):
        """Display the okay and cancel buttons.
           This section will give you the okay
           and cancel button to start your
           rendering or cancel it"""
        # Define this section layout
        okay_cancel_layout = QHBoxLayout()
        # Create the buttons
        self.okay_button = QPushButton("Okay")
        self.cancel_button = QPushButton("Cancel")
        # Add the widgets to the layout
        okay_cancel_layout.addWidget(self.okay_button)
        okay_cancel_layout.addWidget(self.cancel_button)
        # Add this layout section to the general layout
        self.general_layout.addLayout(okay_cancel_layout)

    def main(self):
        """This function calls the create_camera function from the
           TurntableController class ands creates the camera and get the values
           from the distance_Slider, the height_slider and the interval_combo_box
           to set the default camera values
        """

        TurntableController.create_camera(self.distance_slider.value(), TurntableController.get_object_name())
        TurntableController.create_rotation(self.interval_angle_selector.currentText())


if __name__ == "__main__":

    if not cmds.ls(sl=True):
        cmds.error("Select an object")

    elif cmds.ls("camera_render1"):
        cmds.warning("There is a camera_render1 and an offset created already, check your maya windows")
        cmds.delete("camera_render1", "offset_cameraRender1")
        cmds.select("pSphere1")
        turn_table_view.main()
        turn_table_view.show()
    else:
        try:
            turn_table_view.close()  # pylint: disable=E0601
            turn_table_view.deleteLater()

        except:
            pass

        turn_table_view = TurntableView()
        turn_table_view.main()
        turn_table_view.show()
