[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Dominos-Nuro Autonomous Delivery Car

Project-01 for the course _ENPM662: Introduction to Robot Modeling (Fall 2021)_.

The aim of this project was to model a robot car in SolidWorks from scratch and export it to the Unified Robot Description Format (URDF) with links, joints and transmission blocks along with a LiDAR sensor mounted on the car. Controllers were added to the joints of the car such that the front wheels can be turned and the rear wheels make it move forward, as visualized in ROS's Gazebo and RViz environments.

The robot car was physically modeled with inspiration from Dominos' autonomous delivery car ([Nuro R2](https://www.nuro.ai/), see below picture [^1]), with modified lengths and wheel diameter. The original design credits belong to the mentioned company, and no copyrights infringements were intended as the car was used as reference for educational purposes only.

<p align="center">
  <img src="https://user-images.githubusercontent.com/40534801/190452292-7cc8bebb-735e-4df0-9a05-2d49c22804f6.jpg" width="300" height="150">
</p>



## Delivery Car CAD Model 
<p align="center">
  <img src="https://user-images.githubusercontent.com/40534801/190447697-565531a1-c546-49b5-85bf-ff634952051a.jpg" width="300" height="200">
</p>

All the SolidWorks CAD parts and assembly of the car are in the `/CAD` directory.

## Demos
* ROS Publisher-Subscriber to move the car in straight-line and circular trajectories. 
  <p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/190451553-f21b54bd-c6c7-4e16-baed-29bf2082836c.gif" width="600" height="400">
  </p>

* Visualizing the mounted LiDAR data in RViz. 
  <p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/190458186-2dc943f1-d527-4841-8fad-7197e41cb4b3.gif" width="600" height="400">
  </p>

## Running the Simulation:

Place the `delivery_car` ROS package in the `\src` directory of your catkin workspace and build it using `cd ~/catkin_ws && catkin_make`

**1. For the teleop-demo:**	

In a terminal window, run the follwoing to launch the car in given Gazebo world:
		`roslaunch delivery_car template_launch.launch` 

In another terminal window, run:
    `rosrun delivery_car delivery_car_teleop.py`


**2. For the publisher-subscriber demo:**	

In a terminal window, run the follwoing to launch the car in the given Gazebo world:
		`roslaunch delivery_car template_launch.launch` 

In another terminal window, run the following for the publisher:
    `rosrun delivery_car move_bot_pub.py`
    
In a third terminal window, run the following for the subscriber:
    `rosrun delivery_car move_bot_sub.py`
    
    
    

[^1]: Image Courtesy: https://www.motorauthority.com/news/1131910_domino-s-launches-autonomous-pizza-delivery-with-self-driving-robot-car
