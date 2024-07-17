### ROS SESSION5 ASSIGNMENT : TEMPERATURE MONITORING SYSTEM

## Overview
This project involves the creation of a ROS 2 package(myros1package)for temperature monitoring.
The package includes nodes for publishing random temperature values,made for testing,could be obtained from a temperature sensor for realtime application.Then,subscribing to these values, and logging them to a file 
called temperature_log text file.The nodes are made to interact and communicate with each other.

## Features
# 1-Temperature Publisher Node: 
Generates and publishes random temperature values at regular intervals.
# 2-Threshold Subscriber Node: 
Subscribes to the temperature topic, checks if the temperature exceeds a predefined threshold which is taken 36 for testing, and publishes an alert message if the threshold is exceeded.
# 3-Alert Publisher Node:
Subscribes to the alert message of the threshold subscriber and publishes an alert to another topic.
# 4-Temperature Logger Node: 
Subscribes to the temperature topic and logs the temperature values to a text file saved under temperature_log.txt.

## Usage
1- Clone the repository into your ROS2 workspace
2- Build the package
3- Souce the setup file 
4- You can either run each node alone and communicate using #windows in the terminal:

ros2 run myros1package temperature_publisher
ros2 run myros1package threshold_subscriber
ros2 run myros1package alert_publisher
ros2 run myros1package temperature_logger
  OR use the launch file to run all the nodes together:
ros2 launch myros1package temperature_monitoring_launch.py


ros2 run myros1package temperature_logge
