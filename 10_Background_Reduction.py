'''
background reduction means extracting the moving forground from the static background.
this can also be used to compare two similar images in order to extract the differences between them.
'''

# IMPORTING ALL THE NECESSARY DEPENENCIES AND LIBRARIES
import numpy as np
import cv2

#STARING TO CAPTURE THE VIDEO STREAM FROM DEFAULT WEBCAM
cap = cv2.VideoCapture(0)
foreground_model = cv2.createBackgroundSubtractorMOG2()

while(1):
	#CAPTURING THE FRAME AND READING IT
    ret, frame = cap.read()

    #DEFINING A MASK TO BE APPLIED
    foregroundmask = foreground_model.apply(frame)
 	
 	#OUTPUT THE ORIGINALLY CAPTURED FRAME
    cv2.imshow('frame',frame)
    #OUTPUT THE RESULTING FRAME
    cv2.imshow('foreground',foreground)

    
    #PRESSING 'Q' BUTTON ON KEYBOARD TO QUIT OUT FROM THE WINDOWS
	if cv2.waitKey(20) and 0xFF == ord('q'):
		break

#RELEASING ALL THE CAPTURED VIDEO STREAM(background)
cap.release()
#CLOSING ALL THE OPENED WINDOWS (background)
cv2.destroyAllWindows()