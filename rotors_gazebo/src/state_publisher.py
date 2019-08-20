#!/usr/bin/env python


import rospy

from gazebo_msgs.srv import GetModelState



def state0bject(arg):
    try:
        rospy.init_node('state_publisher',anonymous=True)
        rospy.loginfo("Gettig Model State")
        rate = rospy.Rate(1)
        g_get_state=rospy.ServiceProxy("gazebo/get_model_state",GetModelState)
        rospy.wait_for_service("/gazebo/get_model_state")

        while not rospy.is_shutdown():
            objstate = g_get_state(model_name=arg)
            state = (objstate.pose.position.x, objstate.pose.position.y)
            f = open("statefile.txt","a")
            f.write(str(state)+'\n')
            f.close()
            rate.sleep()

    except rospy.ServiceException as e:
        rospy.loginfo("Get Model State service call failde: {0}".format(e))


if __name__ == '__main__':
    try:
        state0bject('firefly')
    except rospy.ROSInterruptException:
        pass
