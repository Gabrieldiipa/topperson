#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('cmd_vel',  Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    msg = Twist()
    msg.linear.x = input('Lin x: ')
    msg.linear.y = input('Lin y: ')
    msg.linear.z = input('Lin z: ')
    msg.angular.x = input('Ang x: ')
    msg.angular.y = input('Ang y: ')
    msg.angular.z = input('Ang z: ')

   ## while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass