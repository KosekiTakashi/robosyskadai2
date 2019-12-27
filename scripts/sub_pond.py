#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def cb(message):
    print('{0}pond = {1}kg'.format(message.data,message.data * 0.4535))

if __name__ == '__main__':
    rospy.init_node('sub_pond')
    sub = rospy.Subscriber('/pond', Int32, cb)
    rospy.spin()

