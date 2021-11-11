#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float64
from pynput import keyboard
from interbotix_sdk.msg import SingleCommand
#from control.msg import SingleCommand
speed = [-0.075, 0.075]
joint = ['waist', 'shoulder', 'elbow', 'wrist_angle', 'gripper']
keys = ['w', 's', 'e', 'd', 'r', 'f', 't', 'g', 'y', 'h']

class KeyPublisher:

	
    def __init__(self):
        rospy.loginfo("Starting the node key_publisher") #Info that may be useful to a user. See ROS Verbosity Levels
        rospy.init_node("key_publisher", anonymous=True) #Initialize key_publisher node

        #Create a publisher to the keypress topic
        #rospy Publisher Initialization:
        #pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10)
        self.key_publisher = rospy.Publisher('/px100/single_joint/command', SingleCommand, queue_size=100)


    def publish_key(self, key, data):
        msg = SingleCommand()
        msg.joint_name = data[0]
        msg.cmd = data[1]
        print('joint_name: {0}    cmd: {1}'.format(data[0], data[1]))
        #print(key)
        self.key_publisher.publish(msg)


    def on_press(self, key):
        if key == keyboard.Key.esc: #If 'esc' is pressed, stop the listener
            return False
        
        try:
            k = key.char
        except:
            k = key.name
        
        if k in keys:
            print('Key pressed: {0}'.format(key)) #Print pressed key
            data = data_format(key)
            
            self.publish_key(key, data)
        
    def on_release(self, key):
        
        if key == keyboard.Key.esc: #If 'esc' is pressed, stop the listener
            return False

        try:
            k = key.char
        except:
            k = key.name
        
        if k in keys:
            print('Key released: {0}'.format(key))
            data = data_format(key)
            data[1] = 0
            self.publish_key(key, data)
    
    def keyboard_listener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

def data_format(key):
    data = []
    if(key.char == 'w'):
        data = ['waist', speed[1]]
        return data
    if(key.char == 's'):
        data = ['waist', speed[0]]
        return data

    if(key.char == 'e'):
        data = ['shoulder', speed[1]]
        return data
    if(key.char == 'd'):
        data = ['shoulder', speed[0]]
        return data

    if(key.char == 'r'):
        data = ['elbow', speed[1]]
        return data
    if(key.char == 'f'):
        data = ['elbow', speed[0]]
        return data

    if(key.char == 't'):
        data = ['wrist_angle', speed[1]]
        return data
    if(key.char == 'g'):
        data = ['wrist_angle', speed[0]]
        return data

    if(key.char == 'y'):
        data = ['gripper', speed[1]]
        return data
    if(key.char == 'h'):
        data = ['gripper', speed[0]]
        return data


def main():
    key_publisher = KeyPublisher()
    key_publisher.keyboard_listener()

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Stopping key:_publisher")

if __name__ == '__main__':
    main()
