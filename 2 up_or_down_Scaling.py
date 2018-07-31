#IMPORTING NECESSARY DEPENDENCIES AND LIBRARIES
import numpy as np
import cv2

#STARING TO CAPTURE THE VIDEO STREAM FROM DEFAULT WEBCAM
cap = cv2.VideoCapture(0)

#FUNCTION TO RESCALE THE FRAME TO DESIRED PERCENTAGE
def rescale_frame(frame, percentage = 75):
	#WIDTH OF THE FRAME
	width = int(frame.shape[1] * percent / 100)
	#HEIGHT OF THE FRAME
	height = int(frame.shape[0] * percent / 100)
	#DIMENTIONS
	dim = (width, height)

	return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

while True:

	#CAPTURING THE FRAME AND READING IT
	frame, ret = cap.read()

	#SETTING THE FRAME SCALE TO 75% OF THE ORIGINAL SCALE
	frame75 = rescale_frame(frame, percentage = 75)
	cv2.imshow('frame75', frame75)

	#SETTING THE FRAME SCALE TO 150% OF THE ORIGINAL SCALE
	frame150 = rescale_frame(frame, percentage = 150)
	cv2.imshow('frame150', frame150)
	
	#PRESSING 'Q' BUTTON ON KEYBOARD TO QUIT OUT FROM THE WINDOWS
	if cv2.waitKey(0) and 0xFF == ord('q'):
		break

#RELEASING ALL THE CAPTURED VIDEO STREAM
cap.release()
#CLOSING ALL THE OPENED WINDOWS FROM BACKGROUND
cv2.destroyAllWindows()