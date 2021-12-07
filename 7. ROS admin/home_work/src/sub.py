#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("welcome_sub_node")

def callback(msg):
    print(msg)

rospy.Subscriber("welcome_topic", String, callback)
rospy.spin()
