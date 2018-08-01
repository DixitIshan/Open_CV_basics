#IMPORTING NECESSARY DEPENDENCIES
import numpy as np
import cv2

#STARTING THE VIDEO STREAM FROM THE WEBCAM
cap = cv2.VideoCapture(0)

while True:
	#'_'(UNDERSCORE) IS THE PYTHON CONVENTION TO LET USERS KNOW THAT THERE IS VALUE IN IT BUT IT IS TO BE NEGLECTED FOR THIS CASE
	_, frame = cap.read()

	# HSV stands for 'Hue', 'Saturation' and 'Value'
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #DEFINING THE THRESHOLDS FOR RANGE
    lower_threshold = int(max(0, (1.0 - 0.33) * median))
	upper_threshold = int(min(255, (1.0 + 0.33) * median))

    #DETECTING THE EDGES IN THE RANGE OF LOWER AND UPPER THRESHOLDS
    edges = cv2.Canny(frame,lower_threshold,upper_threshold)

    #OUTPUT THE ORIGINALLY CAPTURED FRAME
    cv2.imshow('Original',frame)
    
    #OUTPUT THE RESULTING FRAME
    cv2.imshow('Edges',edges)

	#PRESSING 'Q' BUTTON ON KEYBOARD TO QUIT OUT FROM THE WINDOWS
	if cv2.waitKey(20) and 0xFF == ord('q'):
		break


#RELEASING ALL THE CAPTURED VIDEO STREAM
cap.release()
#CLOSING ALL THE OPENED WINDOWS FROM BACKGROUND
cv2.destroyAllWindows()
