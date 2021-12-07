import rospy
import actionlib

from actionlib_tutorials.msg import FibonacciAction, FibonacciGoal

def action_feedback(fb):
    print(fb)

def fibonacci_client():

    client = actionlib.SimpleActionClient('fibonacci', FibonacciAction)
    client.wait_for_server()
    client.send_goal(FibonacciGoal(order=5), feedback_cb=action_feedback)

    client.wait_for_result()

    return client.get_result()

rospy.init_node('fibonacci_client')
result = fibonacci_client()

print("Have result:")
print(result)