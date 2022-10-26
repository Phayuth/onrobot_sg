from sgdrv import SG

sg = SG("192.168.1.1",502) #init connection to the gripper

sg.set_model_id(3)  # select the model of the gripper
sg.set_init()       # init gripper
sg.set_gentle(True) # or sg.set_gentle_off() , to set the gripper force to gentle on or off
sg.get_gp_wd()      # show the current width of the gripper
sg.set_target(500)  # set gripper position before moving it min =100 and max=750
sg.set_move()       # start moving command
sg.get_status()
sg.get_gp_max_wd()
sg.get_gp_min_wd()

sg.close_connection() # close connection to gripper