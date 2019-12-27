#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray

rospy.init_node('pub_num')
pub_num = rospy.Publisher('/num', Int32MultiArray, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    x = int(raw_input('input x:'))
    y = int(raw_input('input y:'))
    num = [x,y]
    num = Int32MultiArray(data = num)
    pub_num.publish(num)
    rate.sleep()
