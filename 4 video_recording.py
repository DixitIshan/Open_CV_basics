#IMPORTING NECESSARY DEPENDENCIES AND LIBRARIES
import os
import numpy as numpy
import cv2

#naem of the saved file
filename = 'video.avi'
#FPS = 24.0 IS IDEAL FOR 720P
frames_per_seconds = 24.0
#DEFINING THE RESOLUTION
my_res = '720p'

#STARING TO CAPTURE THE VIDEO STREAM FROM DEFAULT WEBCAM
cap = VideoCapture(0)

#A FUNCTION TO SET THE WIDTH AND HEIGHT OF THE FRAME
def change_resolution(cap, width, height):
	cap.set(3, width)
	cap.set(4, height)

#A DICTIONARY THAT CONTAINS WIDTH AND HEIGHT OF THE RESOLUTION IN STRING FORMAT
STD_DIM = {
	"480p" : (640, 480),
	"720p" : (1280, 720),
	"1080p" : (1920, 1080),
	"4k" : (3840, 2160),
}


#FUNCTION TO SET THE DIMENTIONS OF THE FRAME AND RESOLUTION OF THE OUTPUT
def set_dimensions(cap, res = '1080p'): #DEFAULT AND CAN BE CHANGED ACCORDING TO NECESSITY
	width, height = STD_DIM['480p'] #DEFAULT AND CAN BE CHANGED ACCORDING TO NECESSITY
	if res in STD_DIM:
		width, height = STD_DIM[res]
	change_resolution(cap, width, height)
	return width, height


#TYPE OF VIDEO FILE AND ITS EXTENTION
'''
Video Encoding, might require additional installs
Types of Codes: http://www.fourcc.org/codecs.php

also OpenCV 2 doesn't support cv2.VideoWriter_fourcc. Instead use cv2.cv.CV_FOURCC(*'XVID')
'''
VIDEO_TYPE = {
	'avi' : cv2.VideoWriter_fourcc(*'XVID')
	'mp4' : cv2.VideoWriter_fourcc(*'XVID')
	'mp4' : cv2.VideoWriter_fourcc(*'H264')
}


# FUNCTION TO SET THE TYPE OF THE VIDEO FILE. DEFAULT IS 'avi'
def set_videotype(filename):
	filename, ext = os.path.splitext(filename)
	if ext in VIDEO_TYPE:
		return VIDEO_TYPE[ext]
	return (VIDEO_TYPE['avi'])


dims = set_dimensions(cap, res = my_res)
video_type_cv2 = set_videotype(filename)


#PASSING IN THE PARAMETERS TO OUPUT THE STREAMING FILE TO THE VIDEO WRITER OF CV2
out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims)


while True:

	#CAPTURING THE FRAME AND READING IT
	ret, frame = cap.read()
	out.write(frame)

	#OUTPUT THE ORIGINALLY CAPTURED FRAME
	cv2.imshow('frame', frame)

	#PRESSING 'Q' BUTTON ON KEYBOARD TO QUIT OUT FROM THE WINDOWS
	if cv2.waitKey(20) and 0xFF == ord('q'):
		break

#RELEASING ALL THE CAPTURED VIDEO STREAM(background)
cap.release()
#RELEASING THE VIDEO WRITER WINDOW FROM BACKGROUND
out.release()
#CLOSING ALL THE OPENED WINDOWS (background)
cv2.destroyAllWindows()