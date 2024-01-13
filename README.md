[//]:<> (This is a comment)


# Turntable Tool

[//]:<> (This is a comment)
This maya tool allows the artists to create a turntable
automatically which is a camera that rotates around the selected
object and creates a little animation of the camera view moving around
the selected object. Here is a look at the User Interface:

[//]:<> (This is an image)

![](Images/Screen%20Shot%202022-11-01%20at%2014.08.58.png)

=======================================================
## Note:

This tool was tested and developed using MAYA 2020.4 on a windows machine

=======================================================
# INSTALLATION

When you download the file you are going to see a folder with the name of "Turntable_tool", 
you can go and paste it in your script folders in your Maya folder. The folder has an __init( )__
file, the file is for you to be able to import the other scripts into the main script.


In case there is not an init file in the folder, just create an empty one and you should be good to go.

__As for the shelf button__, just create one by dragging the file "turntable_tool_shelf_bttn" to your customized shelves

=======================================================
##About the code

It has 3 files, the "turntable_controller", "turntable_gui" and "turntable_tool_shelf_bttn"

The gui calls the controller functions from the controller class, that is why it is important to 
make sure the "turntable_controller" script is being imported into the GUI script

The "turntable_tool_shelf_bttn" script is the one you are going to turn into a shelf button.

It is a really simple script just imports the turntable_gui and calls the "show_turntable( )" method.



=======================================================

##Sections
It has 5 sections, from top to bottom they are:

[//]:<> ()
*The display section*

*The control distance section*

*The height control section*

*The set interval section*

*The Okay_and_Cancel section*

=======================================================
> Q. How does it work?

> A. First, select an object and then just click on the shelf button. Use the Cancel button to delete everything that
> was created by the tool and use the okay button when you are okay (pun intended) with the selected values.
> 
> You can preview the animation without closing the tool.
> You can find a video on the use of the tool in the folder.
>
**IMPORTANT:**
> Q. How do I change the values?

>A. Just move the sliders and choose the degrees per frame from the combobox
> DO NOT close the tool until you are okay with the values.
> Remember that the values can be changed only while the tool is open.
> You can preview it by clicking the play button in your timeline.


![](Images/Gifs/Turntable_tool_Juan_Cruz_AdobeExpress.gif)

*NOTE:*
Make sure your timeline has enough frame length, otherwise, the camera animation
will look incomplete. Just make sure you have at least 180 frames in your timeline. Since the
smallest interval value is 2 degrees, you need 180 frames in your timeline, 
since it will rotate 2 degrees per frame.

![](Images/Gifs/Enough_Frames_AdobeExpress.gif)


#Author and contact info

Juan J. Cruz Rosales - email: silbitron@gmail.com


