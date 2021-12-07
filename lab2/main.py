import rospy
from mover import RoboMover
from photo import RoboPhotographer
from turner import RoboTurner

rospy.init_node("RoboMover")

rm = RoboMover()
rp = RoboPhotographer()
rt = RoboTurner()

rm.move_to_target(1,1)
rt.search_the_ball()
rp.take_picture()
rm.move_to_target(0,0) 
