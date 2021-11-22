#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from ball_chaser.srv import DriveToTarget
from ball_chaser.srv import DriveToTargetResponse

def drive_to_target(req):
    motor_command_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    motor_command = Twist()
    motor_command.linear.x = req.linear_x
    motor_command.linear.y = 0
    motor_command.linear.z = 0
    motor_command.angular.x = 0
    motor_command.angular.y = 0
    motor_command.angular.z = req.angular_z
    
    motor_command_publisher.publish(motor_command)
    s = "linear: "+str(motor_command.linear.x)+" "+"angular: "+ str(motor_command.angular.z)
    return s
    
def drive_bot_server():
    rospy.init_node('drive_bot')
    print("Initialize a ROS node named drive_bot.")
    s = rospy.Service('/ball_chaser/command_robot', DriveToTarget, drive_to_target)
    print("Ready to drive to target.")
    rospy.spin()

if __name__ == "__main__":
    drive_bot_server()
