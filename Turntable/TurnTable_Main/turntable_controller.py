import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as omui


class TurntableController(object):
    """Turntable controller methods and logic
        Args:
            object(optional): It is recommended that in python 2 we use the "new style" class
    """

    @classmethod
    def create_camera(cls, distance_slider_value, maya_object):
        """
        Function to create the camera "camera_render1" and the offset
        and set their different attributes
        Args:
            distance_slider_value(int): Value from the distance slider widget
            maya_object(str): The name from the selected object
        """
        cmds.camera(name="camera_render1")
        cmds.setAttr("camera_render1.translateZ", distance_slider_value)
        cmds.group(name="offset_cameraRender1", em=True)
        cmds.parent("camera_render1", "offset_cameraRender1")
        cmds.matchTransform("offset_cameraRender1", maya_object, pos=True)

    @classmethod
    def get_object_name(cls):
        """
        Function that get the name of the selected object.
        Returns:
                str: The name of the first item in the list, which is a polygon
        """
        return cmds.ls(sl=True)[0]

    @classmethod
    def create_rotation(cls, cobox_value):
        """
        Function that get the name of the selected object.
        Args:
            cobox_value(str): Value displayed in the combo_box widget.
        """
        degrees = float(cobox_value)

        first_keyframe = cmds.currentTime(q=True)
        second_keyframe = first_keyframe + 1

        cmds.setKeyframe("offset_cameraRender1", at="rotateY", v=0, t=first_keyframe, itt="linear", ott="linear")
        cmds.setKeyframe("offset_cameraRender1", at="rotateY", v=degrees, t=second_keyframe, itt="linear", ott="linear")
        cmds.setInfinity("offset_cameraRender1", attribute="rotateY", postInfinite="cycleRelative")
        cmds.setInfinity("offset_cameraRender1", attribute="rotateY", preInfinite="cycleRelative")

    @classmethod
    def delete_rotation(cls):
        """
        Delete the keyframes created in the offset_cameraRender1
        """
        cmds.cutKey("offset_cameraRender1")

    @classmethod
    def set_traslation(cls, distance_value):
        """
        Makes the camera move on the Z axis, depending on the value
        of the distance slider
        Args:
            distance_value(int): Value gotten from the distance slider,
            depending on the number, the cameras height will change
        """
        cmds.setAttr("camera_render1.translateZ", distance_value)
        # print(distance_value)

    @classmethod
    def set_height(cls, height_value):
        """
        Makes the camera move on the Y axis, depending on the value
        of the height slider
        Args:
            height_value(int): Value gotten from the height slider,
            depending on the number, the cameras height will change
        """
        cmds.setAttr("camera_render1.translateY", height_value)
        # print(height_value)

    @classmethod
    def cancel(cls, exit_func):
        """
        Exits the UI and delete the created camera and its offset
        Args:
            exit_func(Function): Close() function inherited from QWidget
        """
        cmds.delete("camera_render1", "offset_cameraRender1")
        exit_func
