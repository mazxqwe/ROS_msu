#!/usr/bin/env python3

import rospy
import actionlib

from home_work.msg import FibonacciActionAction, FibonacciActionGoal

def action_feedback(fb):
    print(fb)

def fibonacci_client():

    client = actionlib.SimpleActionClient('fibonacci', FibonacciActionAction)
    client.wait_for_server()
    client.send_goal(FibonacciActionGoal(order=5), feedback_cb=action_feedback)

    client.wait_for_result()

    return client.get_result()

rospy.init_node('fibonacci_client')
result = fibonacci_client()

print("Have result:")
print(result)
