#!/usr/bin/env python3

import rospy 
from home_work.srv import AddTwoInts,AddTwoIntsResponse

def add_two_ints(req):
    sum = req.a + req.b
    print("Returning [%s + %s = %s]" % (req.a, req.b, sum))
    return AddTwoIntsResponse(sum)

rospy.init_node("add_server_node")
s = rospy.Service('add_two_ints', AddTwoInts, add_two_ints)
rospy.spin()