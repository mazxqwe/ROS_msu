import rospy, math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class Turtle():

    const_angular_z = 1.7
    delta = 0.1

    def __init__(self):
        rospy.on_shutdown(self.shutdown)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=111)
        rospy.Subscriber("turtle1/pose", Pose, self.pose_callback)
        self.pose = None
        self.angular_z = Turtle.const_angular_z
        self.prev_qtr = None

    def shutdown(self):
        self.pub.publish(Twist())

    def pose_callback(self, pose):
        self.pose = pose

    def wait_turtle(self):
        while self.pose is None:
            rospy.loginfo('Wait turtle')
            rospy.sleep(0.1)

    def return_theta(self, theta, qtr):
        cmd_vel = Twist()

        if self.prev_qtr != qtr:
            self.prev_qtr = qtr
            self.angular_z = Turtle.const_angular_z
 
        while not rospy.is_shutdown():
            if (abs(self.pose.theta) < theta) and (qtr==1 or qtr==2) or \
               (abs(self.pose.theta) > theta) and (qtr==3 or qtr==4):
                cmd_vel.angular.z = \
                self.angular_z = self.delta if self.angular_z <= self.delta else self.angular_z - self.delta
                self.pub.publish(cmd_vel)
            else:
                cmd_vel.angular.z = 0
                self.pub.publish(cmd_vel)
                return
            rospy.sleep(0.1)

    def move_forward(self, dist):
        start_pose = self.pose
        move_dist = 0
        cmd_vel = Twist()

        while not rospy.is_shutdown():
            move_dist = self.getMoveDist(start_pose, self.pose)
            if (move_dist < dist):
                cmd_vel.linear.x = 1
                self.pub.publish(cmd_vel)
            else:
                cmd_vel.linear.x = 0
                self.pub.publish(cmd_vel)
                return
            rospy.sleep(0.2)

    def getMoveDist(self, start_pose, current_pose):

        move_dist = math.sqrt(math.pow(start_pose.x - current_pose.x,2) + 
                              math.pow(start_pose.y - current_pose.y,2))

        rospy.loginfo("Dist :%s", move_dist)
        return move_dist

    def move_sqr(self):
        rad = {1: math.pi/2, 2: math.pi - self.delta/10, 3: math.pi/2, 4: 0 + self.delta/10}
        for i in range(1,5):
            turtle.move_forward(3)
            turtle.return_theta(rad[i], i)


if __name__ == '__main__':
    rospy.init_node('move_forward')
    rospy.loginfo("Start Node")

    turtle = Turtle()
    turtle.wait_turtle()
    turtle.move_sqr()
