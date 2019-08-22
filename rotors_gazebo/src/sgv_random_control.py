#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
import random


"""
Function: pub Msh
"""
def pub_msg(pose_msg):
	pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size = 10)
	rospy.init_node('pose_msg_example', anonymous = True)
	#rate = rospy.Rate(10)
	#while not rospy.is_shutdown():
	pub.publish(pose_msg)
		#rate.sleep()

"""
Function:
"""
def Set_SGV_Twist(Twist, linear_x = 0.0, angular_z = 0.0):
	Twist.linear.x = linear_x
	Twist.linear.y = 0.0
	Twist.linear.z = 0.0
	Twist.angular.x = 0.0
	Twist.angular.y = 0.0
	Twist.angular.z = angular_z
	return Twist






if __name__ == '__main__':
	print("run file: " + __file__)
	myTwist = Twist()
	x=0.4
	z=0
	flag=0
	while True:
		linear_x =random.normalvariate(x,0.1)
		angular_z = random.normalvariate(z,0.3)
		while flag<40:
			myTwist = Set_SGV_Twist(myTwist, linear_x,angular_z)
			pub_msg(myTwist)
			time.sleep(0.1)
			flag=flag+1
		print("x,z\n",x,z)
		x=linear_x
		z=angular_z
		if z >1 :
			z=z-1
		if z<-1 :
			z=z+1
		if x>1 :
			x=x-1
		if x<-1 :
			x=x+1

		flag=0

