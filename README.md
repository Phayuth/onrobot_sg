# onrobot Soft Gripper ROS Package
This package is written based on package from [Assistant Prof. takuya-ki](https://github.com/takuya-ki). I worked on UR5 Robot with onrobot-sg gripper and I want use ROS to control it but ROS package for onrobot-sg is nowhere to be found on the internet. So, I decided to wrote one and share it. [for mom!]


### Note
This package is written to work on ROS Melodic (Python 2.7). But with some modification, It could work with modern ROS as well (Noetic Python 3, or ROS 2).


## Requirement
pymodbus
```
sudo pip install pymodbus==2.5.3
```
and make sure it is working properly by import it to python terminal ``` import pymodbus ```


## Installation
```
mkdir -p ws_gripper/src
cd ws_gripper/src
git clone 
cd ..
catkin_make
```
Then source the workspace
```
source ~/ws_gripper/devel/setup.bash
```


## Usage
Bring up the gripper
```
roslaunch onrobot_sg bringup_gripper.launch
```
Control the gripper via rosservice, where desired width is between 110mm and 800 mm
```
rosservice call /cmd_gripper "cmd_width = {desired width}"
```
Control via client service
```
rosrun onrobot_sg cmd_client.py
```


## Reference
- https://github.com/Osaka-University-Harada-Laboratory/onrobot
- https://github.com/takuya-ki/onrobot-vg
- https://github.com/takuya-ki/onrobot-rg
