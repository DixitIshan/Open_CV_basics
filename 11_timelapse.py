# IMPORTING ALL THE NECESSARY LIBRARIES
import os
import numpy as np
import cv2
# IMPORTING THE LIBRARIES RELATED TO TIME AND DATE
import time
import datetime
# GLOB IS UNIX STYLE PATHNAME PATTERN EXPANSION
import glob

# SETTING UP THE VIDEO CONFIGURATIONS

my_res = '480p'
filename = 'video.avi'

# A DICTIONARY THAT CONTAINS WIDTH AND HEIGHT OF THE RESOLUTION IN STRING FORMAT
STD_DIM = {
    "480p" : (640, 480),
    "720p" : (1280, 720),
    "1080p" : (1920, 1080),
    "4k" : (3840, 2160),
}

# TYPE OF VIDEO FILE AND ITS EXTENTION
'''
Video Encoding, might require additional installs
Types of Codes: http://www.fourcc.org/codecs.php

also OpenCV 2 doesn't support cv2.VideoWriter_fourcc. Instead use cv2.cv.CV_FOURCC(*'XVID')
'''
VIDEO_TYPE = {
    'avi' : cv2.VideoWriter_fourcc(*'XVID'),
    'mp4' : cv2.VideoWriter_fourcc(*'XVID'),
    'mp4' : cv2.VideoWriter_fourcc(*'H264'),
}

# A FUNCTION TO SET THE WIDTH AND HEIGHT OF THE FRAME
def change_resolution(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# FUNCTION TO SET THE DIMENTIONS OF THE FRAME AND RESOLUTION OF THE OUTPUT
def set_dimensions(cap, res = '1080p'): #DEFAULT AND CAN BE CHANGED ACCORDING TO NECESSITY
    width, height = STD_DIM['480p'] #DEFAULT AND CAN BE CHANGED ACCORDING TO NECESSITY
    if res in STD_DIM:
        width, height = STD_DIM[res]
    change_resolution(cap, width, height)
    return width, height

# FUNCTION TO SET THE TYPE OF THE VIDEO FILE. DEFAULT IS 'avi'
def set_videotype(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return (VIDEO_TYPE['avi'])

# source: https://stackoverflow.com/a/44659589
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # INITIALIZE THE DIMENSIONS OF THE IMAGE TO BE RESIZED AND GRAB THE IMAGE SIZE
    dim = None
    (h, w) = image.shape[:2]
    
    # IF BOTH THE WIDTH AND HEIGHT ARE NONE, THEN RETURN THE ORIGINAL IMAGE
    if width is None and height is None:
        return image
    
    # CHECK TO SEE IF THE WIDTH IS NONE
    if width is None:
        # CALCULATE THE RATIO OF THE HEIGHT AND CONSTRUCT THE DIMENSIONS
        r = height / float(h)
        dim = (int(w * r), height)
    
    # OTHERWISE, THE HEIGHT IS NONE
    else:
        # CALCULATE THE RATIO OF THE WIDTH AND CONSTRUCT THE DIMENSIONS
        r = width / float(w)
        dim = (width, int(h * r))

    # RESIZE THE IMAGE
    resized = cv2.resize(image, dim, interpolation = inter)
    
    # RETURN THE RESIZED IMAGE
    return resized

# STARING TO CAPTURE THE VIDEO STREAM FROM DEFAULT WEBCAM
cap = cv2.VideoCapture(0)

# DEFINING THE FPS
frames_per_seconds = 20

# CREATING A PATH TO SAVE THE OUTPUT TIMELAPSE VIDEO
save_path='saved-media/video.avi'

# CREATING THE CONFIGURATIONAL SETTING FOR THE VIDEO
# config = CFEVideoConf(cap, filepath=save_path, res='720p')
dims = set_dimensions(cap, res = my_res)
video_type = set_videotype(filename = filename)

# PASSING IN THE PARAMETERS TO OUPUT THE STREAMING FILE TO THE VIDEO WRITER OF CV2
out = cv2.VideoWriter(save_path, video_type, frames_per_seconds, dims)

# CREATING A PATH TO SAVE THE CAPTURED OUTPUT TIMELAPSE FRAMES
timelapse_img_dir = 'images/timelapse'

# TOTAL DURATION OF THE TIMELAPSE CAPTURING PROCESS
seconds_duration = 20

# TIME DIFFERENCE BETWEEN EACH SINGLE IMAGE CAPTURED
seconds_between_shots = .25

# DOUBLE CHECKING ON THE PATH
if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

# DOUBLE CHECKING ON THE PATH
if not os.path.exists(save_path):
    os.mkdir(save_path)

# OUTPUTS THE CURRENT TIME OF THE SYSTEM
now = datetime.datetime.now()

# THIS IS THE TOTAL FUTURE TIME FROM THE CURRENT TIME
finish_time = now + datetime.timedelta(seconds=seconds_duration)

i = 0

# STARTING THE WHILE LOOP EVERY TIME WITH CURRENT TIME AND COMPARING IT WITH FINISHED(FUTURE) TIME
while datetime.datetime.now() < finish_time:
    '''
    Ensure that the current time is still less than the preset finish time
    '''
    ret, frame = cap.read()
    filename = "{}/{}.jpg".format(timelapse_img_dir, i)
    # filename = f"{timelapse_img_dir}/{i}.jpg"
    i += 1
    cv2.imwrite(filename, frame)
    time.sleep(seconds_between_shots)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# CONVERTING ALL THE CAPTURED IMAGES TO A VIDEO
def images_to_video(out, image_dir, clear_images=True):
    image_list = glob.glob(image_dir + "/*.jpg")
    # SORTING THE CAPTURED IMAGES IN ASCENDING ORDER
    sorted_images = sorted(image_list, key=os.path.getmtime)
    # CREATING A VIDEO FROM ALL THE CAPTURED IMAGES.
    # HERE 'FILE' REPRESENTS FILE PATH AND NOT THE FILE ITSELF
    for file in sorted_images:
        image_frame  = cv2.imread(file)
        out.write(image_frame)
    if clear_images:
        '''
        REMOVE STORED TIMELAPSE IMAGES
        '''
        for file in image_list:
            os.remove(file)

# CALLING THE FUNCTION TO MAKE A TIMELAPSE VIDEO
images_to_video(out, timelapse_img_dir)

# WHEN EVERYTHING DONE, RELEASE THE CAPTURE
cap.release()
out.release()
cv2.destroyAllWindows()