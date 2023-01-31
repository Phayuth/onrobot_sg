#! /usr/bin/env python

import rospy
from sgdrv import SG
from onrobot_sg.msg import onrobotsg_read_msg

sg = SG("192.168.1.1",502) #init connection to the gripper

sg.set_model_id(3)
sg.set_init()

rospy.init_node("sg_gripper/stat")

pub = rospy.Publisher("/sg_gripper/status", onrobotsg_read_msg, queue_size = 1)

rate = rospy.Rate(100)
stat =  onrobotsg_read_msg()

while not rospy.is_shutdown():
	
	stat.gripper_width = sg.get_gp_wd()
	stat.status = sg.get_status()
	stat.max_width = sg.get_gp_max_wd()
	stat.min_width = sg.get_gp_min_wd()

	pub.publish(stat)
	rate.sleep()