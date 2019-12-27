#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('pub_pond')
pub = rospy.Publisher('/pond', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n = int(raw_input('input pond:'))
    pub.publish(n)
    rate.sleep()
