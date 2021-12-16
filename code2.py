#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):

	rospy.loginfo("our message is:" + data.data)


def subs():
	rospy.init_node('listener', anonymous=False)

	rospy.Subscriber('robotics_first_topic', String, callback)
	rospy.spin()


if __name__ == "__main__":
	subs()