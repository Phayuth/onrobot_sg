#!/usr/bin/env python

from __future__ import print_function
import rospy
from sgdrv import SG
from onrobot_sg.msg import onrobotsg_read_msg
from onrobot_sg.srv import onrobotsg_cmd_srv,onrobotsg_cmd_srvResponse

# Color class for print in color
class bcolors:
	HEADER    = '\033[95m'
	OKBLUE    = '\033[94m'
	OKCYAN    = '\033[96m'
	OKGREEN   = '\033[92m'
	WARNING   = '\033[93m'
	FAIL      = '\033[91m'
	ENDC      = '\033[0m'
	BOLD      = '\033[1m'
	UNDERLINE = '\033[4m'

def handle_cmd(req):
	print("Req width is %s"%req.cmd_wd)
	sg.set_target(req.cmd_wd)
	sg.set_move()
	return onrobotsg_cmd_srvResponse("Done")

def start():
	rospy.init_node('gripper_cmd')
	rospy.Service('gripper_cmd', onrobotsg_cmd_srv, handle_cmd)
	print("Gripper width is 110 to 750")
	print(bcolors.OKGREEN + "Ready to Receive Command" + bcolors.ENDC)
	rospy.spin()

if __name__ == "__main__":
	try:
		ip       = rospy.get_param('/gripper/ip')
		port     = rospy.get_param('/gripper/port')
		model_id = rospy.get_param('/gripper/model_id')
		gent     = rospy.get_param('/gripper/gentle')

		print("Setting Up Connection")
		sg = SG(ip,port)
		sg.set_model_id(model_id)
		sg.set_init()
		sg.set_gentle(gent)

		start()

	except Exception as e:
		raise e
		
	finally:
		sg.close_connection()
		print(bcolors.OKGREEN + "\nGripper connection is disconnected" + bcolors.ENDC)