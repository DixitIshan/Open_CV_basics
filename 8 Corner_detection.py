# IMPORTING ALL THE NECESSARY DEPENENCIES AND LIBRARIES
import numpy as np
import cv2

#READING THE IMAGE AND CONVERTING IT TO GRAY
img = cv2.imread('heregoesyouamazingimage')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#DEFINE CORNER PARAMETERS for SHI-TOMASI CORNER DETECTOR
corners_to_detect = 100
minimum_quality_score = 0.01
minimum_distance = 10


#DEFINE CORNER PARAMETERS for HARRIS CORNER DETECTOR
block_size = 2
aperture = 29
free_parameter = 0.04


#APPLYING SHI-TOMASI CORNER DETECTOR
ST_corners = cv2.goodFeaturesToTrack(gray, corners_to_detect, minimum_quality_score, minimum_distance)
ST_corners = np.float32(corners)


#APPLYING HARRIS CORNER DETECTOR
Harris_corners = cv2.cornerHarris(gray, block_size, aperture, free_parameter)


#MARK CORNERS
Harris_corners = cv2.dilate(detector_responses, None)


# ONLY KEEP DETECTOR RESPONSES GREATER THAN THRESHOLD, MARK AS WHITE
threshold = 0.02
image_bgr[detector_responses > threshold * detector_responses.max()] = [255,255,255]


# DRAW WHITE CIRCLE AT EACH CORNER
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)


#VIEWING THE RESULTING IMAGES
cv2.imshow('ST_corners', ST_corners)
cv2.imshow('Harris_corners', Harris_corners)