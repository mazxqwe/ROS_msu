import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32


class Subscriber:
    def __init__(self, topic_name='/numbers', count_number=5):
        self.topic_name = topic_name
        self.count_number = count_number
        self.sub = rospy.Subscriber(self.topic_name, Int32, self.callback)
        self.pub = rospy.Publisher("/result", Float32, queue_size=10)
        self.lst = []
    
    def callback(self, income_msg):
        if len(self.lst) > self.count_number:
            val = sum(self.lst)/len(self.lst)
            self.pub.publish(val)
            self.lst.clear()
        
        self.lst.append(income_msg.data)
        

if __name__ == '__main__':
    rospy.init_node('subscriber')
    s = Subscriber()
    rospy.spin()
