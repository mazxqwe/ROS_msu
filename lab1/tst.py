import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class TurtleBot:
    def __init__(self):
        self.vel = Twist()
        self.target = 0.3

        rospy.Subscriber("/scan", LaserScan, self.callback)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    def callback(self, scan):
        self.distance = scan.ranges[0]

    def pub_mover(self, vel_x, vel_z):
        self.vel.linear.x = vel_x
        self.vel.linear.z = vel_z
        self.pub.publish(self.vel)

    def reg (self):
        if self.distance < self.target:
            self.pub_mover(0.1, 0)
        else:
            self.pub_mover(0, 0)

if __name__ == "__main__":
     
    rospy.init_node("laser")
    new_robot = TurtleBot()
    
    while not rospy.is_shutdown():
        rospy.sleep(0.2)
        new_robot.reg
