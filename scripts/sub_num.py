#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32MultiArray

def cb(message):
    print("{0} + {1} = {2}".format(message.data[0],message.data[1],message.data[0] + message.data[1]))

if __name__ == '__main__':
    rospy.init_node('sub_num')
    sub = rospy.Subscriber('/num', Int32MultiArray, cb)
    rospy.spin()

