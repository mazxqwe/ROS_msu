#!/usr/bin/env python3

import rospy
import random
from home_work.srv import AddTwoInts, AddTwoIntsRequest

def add_two_ints_client(a, b):
    rospy.wait_for_service('add_two_ints')
    service_client = rospy.ServiceProxy('add_two_ints', AddTwoInts)

    resp = service_client.call(AddTwoIntsRequest(a, b))
    return resp.sum

a = random.randint(-100 , 100)
b = random.randint(-100 , 100)

sum = add_two_ints_client(a,b)
print("%s + %s = %s"%(a, b, sum))
