# Skyxperts Task 2

[![ROS](https://img.shields.io/badge/ROS-Noetic-brightgreen)](http://wiki.ros.org/noetic)
[![Python](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This is the ROS package for Task 2 of the Skyxperts project. The package is designed for real-time camera image sharpening and publishing in a ROS environment. It captures a raw camera feed, applies image sharpening, and publishes the sharpened images to a ROS topic.

![Sharpened Image](images/sharpened_image.png)

## Features

- Captures raw camera images and publishes them to 'raw_camera_topic'.
- Applies real-time image sharpening using a kernel-based filter.
- Publishes sharpened images to 'sharpened_image_topic'.
- Suitable for computer vision, object detection, and image analysis tasks.

## System Requirements

- ROS Noetic
- Python 3
- OpenCV

## Installation

Follow these steps to set up the required environment:

1. Install ROS Noetic by following the official [ROS Noetic Installation Guide](http://wiki.ros.org/noetic/Installation).

2. Install OpenCV using the following command:

   ```bash
   sudo apt-get install python3-opencv

Output and Visualization
The project captures a raw camera feed, sharpens it in real-time, and publishes the sharpened images to 'sharpened_image_topic.' You can use RQT Image View to visualize the sharpened images as they are published.

Code Flow
The code consists of two main nodes: the camera publisher node (camera_publisher_node.py) and the camera subscriber node (camera_subscriber_node.py). The publisher captures raw camera images, while the subscriber applies real-time image sharpening and publishes the results.

Contributing
Contributions to this project are welcome. If you have suggestions or would like to contribute, please fork the repository and create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or support, you can contact the project maintainer:

Name: Fares Fathy
Email: ffathy2004@hotmail.com
GitHub: github.com/ffathy-tdx
