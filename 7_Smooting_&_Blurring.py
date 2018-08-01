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
	color_value_1 = np.arrays([0, 0, 0])
	color_value_2 = np.arrays([255, 255, 255])

	# MASK IS THE RANGE BETWEEN color_value_1 AND color_value_2. SO BASICALLY MASK IS CURRENTLY IDENTICAL TO FRAME
	mask = cv2.inRange(hsv, color_value_1, color_value_2)

	#OPERATING A 'BITWISE-AND' OPERATION ON MASK AND FRAME
	result = cv2.bitwise_and(frame, frame, mask = mask)

	#AVERAGING THE PIXELS
	kernel = np.ones((10,10), np.float32)/100

	# SMOOTHING
	smooth_result = cv2.filter2D(result, -1, kernel)
	
	#BELOW IS THE SHOCASING OF A FEW DIFFERENT TYPES OF BLUR OPEN-CV HAS TO OFFER
	gaussian_blur = cv2.GaussianBlur(result, (10,10), 0)
	median_blur = cv2.medianBlur(result, 10)
	bilateral_blur = cv2.bilateralFilter(result, 10, 75, 75)
	
	#OUTPUT THE DIFFERENT FRAMES
	#IF BY OUTPUTING SO MANY FRAMES SIMULTANEOUSLY YOUR MACHINE STARTS LAGGING, ONLY OUTPUT THE DESIRED FRAME AT A TIME
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', result)
	cv2.imshow('smooth_result', smooth_result)
	cv2.imshow('median_blur', median_blur)
	cv2.imshow('gaussian_blur', gaussian_blur)
	cv2.imshow('bilateral_blur', bilateral_blur)


	if waitKey(20) and 0xFF == ord('q'):
		break

#DESTROYS ALL THE WINDOWS FROM THE BACKGROUND
cv2.destroyAllWindows()
#RELEASES THE DEFAULT WEBCAM USED FOR CAPTURING
cap.release()