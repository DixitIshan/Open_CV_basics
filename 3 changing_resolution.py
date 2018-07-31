#IMPORTING NECESSARY DEPENDENCIES AND LIBRARIES
import numpy as np
import cv2

#STARING TO CAPTURE THE VIDEO STREAM FROM DEFAULT WEBCAM
cap = cv2.VideoCapture(0)

#FUNCTION TO SET THE RESOLUTION TO 1920 X 1080 FRAMES
def make_1080():
	cap.set(3, 1920)
	cap.set(4, 1080)

#FUNCTION TO SET THE RESOLUTION TO 1280 X 720 FRAMES
def make_720():
	cap.set(3, 1280)
	cap.set(4, 720)

#FUNCTION TO SET THE RESOLUTION TO 640 X 480 FRAMES
def make_480():
	cap.set(3, 640)
	cap.set(3, 480)

def change_resolution(width, height):
	cap.set(3, width)
	cap.set(4, height)

make_720()

while True:
	#CAPTURING THE FRAME AND READING IT
	ret, frame = cap.read()
	
	#OUTPUT THE ORIGINALLY CAPTURED FRAME
	cv2.imshow('frame', frame)
	
	#PRESSING 'Q' BUTTON ON KEYBOARD TO QUIT OUT FROM THE WINDOWS
	if cv2.waitKey(20) and 0xFF == ord('q'):
		break


#RELEASING ALL THE CAPTURED VIDEO STREAM
cap.release()
#CLOSING ALL THE OPENED WINDOWS FROM BACKGROUND
cv2.destroyAllWindows()