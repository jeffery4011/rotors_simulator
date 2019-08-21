#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist


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

"""
Function: get Vel from local file
"""
def Get_ugv_vel(Twist_file):
	offset = -3
	last_line = ""
	while True:
		try:
			Twist_file.seek(offset, 2)
		except IOError:
			print("\n\nugv_Twist format invalid\n\n")
			return
		lines = Twist_file.readlines()
		if(len(lines) > 1):
			last_line = lines[-1]
			break
		offset = offset *2
	twist_str = last_line.split(',')
	if(twist_str[0].isdigit and twist_str[1].isdigit):
		linear_x = float(twist_str[0])
		angular_z = float(twist_str[1])
		#print("linear_x = %f, angular_z = %f" % (linear_x, angular_z))
		return linear_x,angular_z
	else:
		print("\n\nugv_Twist format invalid\n\n")
		return


file_location = "ugv_Twist.txt"

if __name__ == '__main__':
	print("run file: " + __file__)
	#ugv_Twist_file = open(file_location, "r")
	myTwist = Twist()
	while True:
		ugv_Twist_file = open(file_location, "r")
		linear_x,angular_z = Get_ugv_vel(ugv_Twist_file)
		ugv_Twist_file.close()
		myTwist = Set_SGV_Twist(myTwist, linear_x,angular_z)
		pub_msg(myTwist)
		time.sleep(0.1)

