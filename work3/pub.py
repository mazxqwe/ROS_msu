import rospy
from std_msgs.msg import Int32
import random


class Publisher:
    def __init__(self, hz=5, start=1,end=99):
        self.hz = 5
        self.start = start
        self.end = end
        self.pub = rospy.Publisher("/numbers", Int32, queue_size=10)
    
    def public_data(self):
        rospy.init_node('publisher')

        while not rospy.is_shutdown():
            self.pub.publish(random.randint(self.start, self.end))
            rospy.sleep(1/self.hz)

if __name__ == '__main__':
    p = Publisher()
    p.public_data()
