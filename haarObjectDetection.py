# in this case, face detection is done using the haar cascade classifier

import cv2
import numpy as np

# we'll load the cascade feature files of face and eyes
faceCascade = cv2.CascadeClassifier('faceHaarCascade.xml')
eyeCascade = cv2.CascadeClassifier('eyeHaarCascade.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # we'll detect in gray image
    faces = faceCascade.detectMultiScale(grayImg, 1.3, 5) # Detection function calling
    for (x,y,w,h) in faces: # creating the rectangle around the face
        # x+w,y+h will be for the total height of the face as detected by the function
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) 
        roiGray = grayImg[y:y+h, x:x+w]
        roiColor = img[y:y+h, x:x+w]
        eyesFound = eyeCascade.detectMultiScale(roiGray, 1.3, 5)
        for(ex,ey,ew,eh) in eyesFound:
            cv2.rectangle(roiColor, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()


