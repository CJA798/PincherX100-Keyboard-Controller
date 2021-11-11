# PincherX100-Keyboard-Controller
##Keyboard controller for the PincherX 100 robotic arm.

W-S control the waist  
E-D control the shoulder  
R-F control the elbow  
T-G control the wrist_angle  
Y-H control the gripper  

The speed values are set in the "speed = [-0.075, 0.075]" line of the controller.py file.  
The default 0.075 would move the joints VERY slow.  

##INSTRUCTIONS:

Plug the PX100 robotic arm  
Find the port using the command dmesg | grep tty  
The port should be in the format /dev/ttyUSB0  

(on a terminal)  
roscore &  
rqt_graph &  

rosrun control set_arm.py  
OR  
run custom set command on a terminal. Check [Usage](https://github.com/Interbotix/interbotix_ros_arms/tree/master/interbotix_sdk#usage) in the Interbotix repository for more info.  

(on a new terminal)  
rosrun control controller.py 



Made by [C.Anzola](https://github.com/CJA798?tab=repositories) 11/11/2021  
Used and/or referenced code from:  
- [kynan](https://stackoverflow.com/questions/11918999/key-listeners-in-python)
- [Drkstr](https://answers.ros.org/question/315716/python-node-for-publishing-keyboard-events/)
- [rospy Tutorials](http://wiki.ros.org/rospy/Tutorials)



