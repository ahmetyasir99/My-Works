#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from dronekit import connect
#connection_string="127.0.0.1:14550"
#iha = connect(connection_string,wait_ready=True,timeout=100)

def publisher():

	pub = rospy.Publisher('robotics_first_topic', String, queue_size = 10)
	rospy.init_node('publisher_node', anonymous = False)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
	#	print(iha.location.global_relative_frame.alt)
		msg = "Our very first publisher code"
		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()

if __name__ == "__main__":
	publisher()


