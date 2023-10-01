#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],  
                       [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened


def image_callback(msg):
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    sharpened = sharpen_image(cv_image)
    sharpened_msg = bridge.cv2_to_imgmsg(sharpened, encoding="bgr8")
    sharpened_pub.publish(sharpened_msg)

if __name__ == '__main__':
    rospy.init_node('image_sharpening_node')
    bridge = CvBridge()
    
    rospy.Subscriber('raw_camera_topic', Image, image_callback)
    sharpened_pub = rospy.Publisher('sharpened_image_topic', Image, queue_size=10)
    
    rospy.spin()

