# IMPORTING ALL THE NECESSARY DEPENENCIES AND LIBRARIES
import cv2
import numpy as np

#CAPTURING THE VIDEO FROM THE DEFAULT WEBCAM
cap = cv2.VideoCapture(0)

while True:
	# ' _ ' IS A PYTHON CONVENTION THAT TELLS THE READER/USER TO IGNORE THE VALUE WHICH IS IN THERE.
	_, frame = cap.read()
	
	#HSV IS IMPORTANT FOR DIFFERENT VALUES AND RANGES OF COLORS INSTEAD OF RGB
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#MAXIMUM AND MINIMUM OF THE COLOR VALUES
	# WE NEED TO CHANGE THE VALUE OF THE FOLLOWING IN ORDER TO GET THE DESIRED RESULTS
	color_value_1 = np.array([0, 0, 0])
	color_value_2 = np.array([255, 255, 255])

	# MASK IS THE RANGE BETWEEN color_value_1 AND color_value_2. SO BASICALLY MASK IS CURRENTLY IDENTICAL TO FRAME
	mask = cv2.inRange(hsv, color_value_1, color_value_2)

	#OPERATING A 'BITWISE-AND' OPERATION ON MASK AND FRAME
	result = cv2.bitwise_and(frame, frame, mask = mask)

	kernel = np.ones((5,5), np.uint8)
	
	'''
	A SLIDER(KERNEL) SLIDES ON THE CAPTURED IMAGE
	IF ALL THE PIXELS IN THE AREA ARE ONE COLORED WITH ONE PIXEL OF DIFFERENT COLOR,
	IT REMOVES THE WHITE PIXEL
	'''
	eroded_img = cv2.erode(mask, kernel, iterations = 1)
	
	#
	dilated_img = cv2.dilate(mask, kernel, iterations = 1)
	
	#OPENING IS THE REMOVING OF FALSE POSITIVES
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	
	#CLOSING IS THE REMOVING OF FALSE NEGATIVES
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	#OUTPUT THE DIFFERENT FRAMES
	#IF BY OUTPUTING SO MANY FRAMES SIMULTANEOUSLY YOUR MACHINE STARTS LAGGING, ONLY OUTPUT THE DESIRED FRAME AT A TIME
	cv2.imshow('frame', frame)
	cv2.imshow('result', result)
	cv2.imshow('eroded_img', eroded_img)
	cv2.imshow('dilated_img', dilated_img)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	if waitKey(20) and 0xFF == ord('q'):
		break

#DESTROYS ALL THE WINDOWS FROM THE BACKGROUND
cv2.destroyAllWindows()
#RELEASES THE DEFAULT WEBCAM USED FOR CAPTURING
cap.release()
