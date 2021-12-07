import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage
from geometry_msgs.msg import Twist

class RoboTurner():

    yellowLower = (14, 180, 80)# dark
    yellowUpper = (34, 255, 255) # light
    ball_not_reached = True
    vel = Twist()
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    
    
    def search_the_ball(self):
        print("Searching the ball")

        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)

        while not rospy.is_shutdown():
            ret,im = cap.read()
            data = self.process(im)
            if data == [0,0,0] or self.ball_not_reached:
                self.go_to_ball(data)
            else:
                cv2.imwrite('ball.jpg', im)
                rospy.loginfo("Picture done")
                break
            rospy.sleep(0.1)


    def process(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.yellowLower, self.yellowUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        self.current_data = [0,0,0]
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius > 10:
                self.current_data = [x,y,radius]
        return self.current_data
    
    def go_to_ball(self, data):
        self.vel.angular.z = -0.4*((data[0]-320)/320)
        if data[2] < 50:
            self.vel.linear.x = 0.05
        else:
            self.vel.linear.x = 0
            self.ball_not_reached = False
        self.pub.publish(self.vel)
