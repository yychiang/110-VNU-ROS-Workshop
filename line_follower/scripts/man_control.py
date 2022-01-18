#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key
    
def main():
    vel = 0
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
    rospy.init_node('manual_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        key = getKey(0.0)
        if key == 'l':
            vel = vel - 0.1
        elif key == 'j': 
            vel = vel +0.1   
        twist = Twist()
        twist.linear.x = 1.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = vel
        
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
