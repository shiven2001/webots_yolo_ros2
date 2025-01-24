# webots_yolo_ros2
Integration of ultralytics yolov8 and newer versions with webots ros2 humble.

Made using Webots Version R2023b and ROS2 Humble. 

Tested on Ubuntu 22.04.

Make sure to intall webots_ros2 first using distributed package

```
sudo apt-get install ros-humble-webots-ros2
```

Using Tiago robot from webot_ws for this repo. Please install ultralytics and dependencies.
```
pip install ultralytics
``
if error regarding numpy version being above 1.X, please downgrade it using

```
pip install numpy==1.26.4
```

or

```
pip install "numpy<2.0" 
```
