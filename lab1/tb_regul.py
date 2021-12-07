import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class RoboMover():

    distance = 0
    distance_prev = 0
    array_of_dp = []
    vel = Twist()

    target = 0.3

    Kp = 3
    Kd = 100
    Ki = 0.1
    dti = 15


    def __init__(self):
        rospy.Subscriber("/scan", LaserScan, self.laser_cb)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    def laser_cb(self, scan):
        self.distance = min(scan.ranges)

    def pub_mover(self, vel_x, vel_z):
        self.vel.linear.x = vel_x
        self.vel.angular.z = vel_z
        self.pub.publish(self.vel)

    def regulator(self):
        v_x = 0.1
        w_z = ((self.target - self.distance)*self.Kp - (self.distance - self.distance_prev) * self.Kd +
                sum(self.array_of_dp) * self.Ki)
        self.pub_mover(v_x, w_z)
        self.distance_prev = self.distance
        if len(self.array_of_dp) < self.dti:
            self.array_of_dp.append(self.target - self.distance)
        else:
            self.array_of_dp.pop(0)
            self.array_of_dp.append(self.target - self.distance)



rospy.init_node("Laser")
m = RoboMover()

while not rospy.is_shutdown():
    rospy.sleep(0.2)
    m.regulator() 
