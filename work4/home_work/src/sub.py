#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node("laser")

def callback(msg):

    for el in msg.ranges:
       print(el)

rospy.Subscriber("scan", LaserScan, callback)
rospy.spin()
