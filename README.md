# Pipeline Defects Detection Crawler (ROS2 + YOLOv11 + Odometry)

## Overview
This project presents an autonomous robotic crawler designed for internal pipeline inspection.  
The system is capable of detecting corrosion, cracks, and obstacles using computer vision based object detection (YOLOv11).  
It integrates real-time localization using wheel encoders and an IMU to estimate the position of detected defects inside the pipeline.  
The robot can be driven manually through a Bluetooth-based teleoperation interface implemented with a ROS2 key publisher node.

---

## Features
- **Real-time defect detection** using YOLOv11  
- **ROS2 modular architecture** for perception, control, and communication  
- **Odometry-based localization** combining encoder and IMU data  
- **Bluetooth teleoperation** for manual driving and testing  
- **Gazebo simulation** for system validation and environment testing  

---

## System Architecture
The system is divided into the following main ROS2 nodes and packages:

| Component | Description |
|------------|-------------|
| `yolo_node` | Handles real-time defect detection using YOLOv11 |
| `control_node` | Receives teleoperation commands and drives motors |
| `odometry-branch` | Computes position from wheel encoders and IMU data |
| `bluetooth_keypublisher` | Publishes velocity commands from Bluetooth input |
| `gazebo_sim` | Provides virtual testing of the robot and sensors |

---

## Technologies Used
- **ROS2 Humble** (Robot Operating System)
- **Gazebo** for simulation and testing
- **YOLOv11** for deep learning object detection
- **Python & C++** for node implementation
- **Bluetooth HC-06** for wireless control
- **Wheel encoders + IMU** for odometry

---

## Directory Structure
