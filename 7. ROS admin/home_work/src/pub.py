#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("welcome_node")

pub = rospy.Publisher("/welcome_topic", String, queue_size=10)

s = String()

msg = rospy.get_param("msg", "")
s.data = msg

while not rospy.is_shutdown():
    pub.publish(s)
    rospy.sleep(1)
