#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from onrobot_sg.srv import *

def cmd_width(cmd):
	rospy.wait_for_service('gripper_cmd')
	try:
		call_srv = rospy.ServiceProxy('gripper_cmd', onrobotsg_cmd_srv)
		resp = call_srv(cmd)
		return resp.cmd_stat
	
	except rospy.ServiceException as e:
		print("Service call failed: %s"%e)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		cmd = int(sys.argv[1])
	else:
		sys.exit(1)
	print(cmd_width(cmd))