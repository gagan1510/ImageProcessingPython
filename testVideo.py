import cv2
import numpy as np

# this is to get the frames of the camera
cap = cv2.VideoCapture(0)
# we can load a video file by using the name of the video file instead of the 0 in parenthesis

# crete a codec of the Writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# creating the object that writes onto the video file 20.0 is the FPS
out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))

# while loop is to capture every frame of the camera until 'q' is pressed
while True:
    ret, frame = cap.read() # to read the instantaneous camera frame
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # make the captured frame grey in color

    # to write each frame onto the file
    out.write(frame)

    cv2.imshow('frame', frame) # display the colored frame
    # cv2.imshow('gray', gray) # display the greyscale frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release() # release the capture object
out.release() 
cv2.destroyAllWindows() # destroy all the window objects displaying the images