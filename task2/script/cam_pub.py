#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('camera_publisher', anonymous=True)
    cap = cv2.VideoCapture(0)
    image_pub = rospy.Publisher('raw_camera_topic', Image, queue_size=10)
    bridge = CvBridge()
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        
        if ret:
            ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_pub.publish(ros_image)
        
        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
