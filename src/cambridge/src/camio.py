#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import cv2
import numpy as np
import os
import time

if __name__ == '__main__':
    rospy.init_node('camio', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    bridge=CvBridge()
    img_pub=rospy.Publisher("camera/image_raw", Image)
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret,frame=cap.read()
        try:
            imgimg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        img_pub.publish(imgimg)
        rate.sleep()