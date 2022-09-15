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



## Demos
* ROS Publisher-Subscriber to move the car in straight-line and circular trajectories. 
  <p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/190451553-f21b54bd-c6c7-4e16-baed-29bf2082836c.gif" width="600" height="400">
  </p>

* Visualizing the mounted LiDAR data in RViz. 
  <p align="center">
    <img src="https://user-images.githubusercontent.com/40534801/190458186-2dc943f1-d527-4841-8fad-7197e41cb4b3.gif" width="600" height="400">
  </p>


[^1]: Image Courtesy: https://www.motorauthority.com/news/1131910_domino-s-launches-autonomous-pizza-delivery-with-self-driving-robot-car

<!-- ## Packages Used
- Python 3.7.11
- Matplotlib 3.5.0
- NumPy 1.21.2

  
## Code Execution

* Clone the repository
  ```
  git clone --recursive https://github.com/adarshmalapaka/autonomous-robotics.git
  ```
