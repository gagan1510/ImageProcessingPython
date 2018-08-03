import cv2
import numpy as np 

# MOG Background removal

# to remove the backgriound, we'll read the changes in each successive frame and 
# then will treat the changing objects as the foreground.
# The places that don't change will be the Background

# capturing the video from the camera
cap = cv2.VideoCapture(0)

# creating an instance of the MOG Background Subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read() # Read frames of the video
    fgmask = fgbg.apply(frame) # apply the background reduction on the frame

    cv2.imshow('inst',frame) # shouwing the instantaneous frame (simple video)
    cv2.imshow('fg', fgmask) # showing the instantaneous bg reduced frame

    k = cv2.waitKey(30) & 0xff # Esc key
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()