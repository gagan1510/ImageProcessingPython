import numpy as np 
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# this will put the RGB value of color of pixel at the coordinate (55,55) in px
px = img[55,55]
print(px)

# we can also change the color of the image at a specific coordinate by initializing it with the color
img[55,55] = [255,255,255]
px = img[55,55]
print(px)

# ROI - Region of Image
# it is the value of all the pixels lying between the provided limits
roi = img[100:150, 100:150]
print(roi)

# change the color of the region of the image
# img[100:150, 100:150] = [255,255,255]

# copy an ROI from one place to another (copy and paste)
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()