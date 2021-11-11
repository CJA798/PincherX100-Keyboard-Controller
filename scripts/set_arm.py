import os
##with open('port.txt', 'r') as f:
  ##  port = f.readline()
port = '/dev/ttyUSB0'

def run():
    
    os.system("roslaunch interbotix_sdk arm_run.launch robot_name:=px100 port:={0} arm_operating_mode:=velocity use_moveit:=true use_default_rviz:=false".format(port))
    #os.system("rosservice /px100/torque_joints_off")

    #print(port)

if __name__ == '__main__':
    run()