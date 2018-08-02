import cv2
import numpy as np
import matplotlib.pyplot as plt

#                  0      corresponds to image grey scale
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# Some other options for imread are: 
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1
# video analysis takes a lot of time to complete in full color

# cv2.imshow('image', img) # (title, image_obj    ``)
# cv2.waitKey(0) # waits for the user to press a key
# cv2.destroyAllWindows() # closes all windows

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show() 

# to write and image into a specific file
cv2.imwrite('watchGrey.png', img)