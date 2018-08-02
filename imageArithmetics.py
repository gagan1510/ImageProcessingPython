import numpy as np
import cv2

img1 = cv2.imread('MPL3D.png')
img2 = cv2.imread('mainlogo.png')

# add 2 images, by simply using the summition operator with the two
# add = img1 + img2 # this adds the two images without letting them lose their opaqueness
# add = cv2.add(img1, img2) # this adds all the pixel values together

# add 2 images on the basis of their %age in the resultant image
# (image1, %(image1), image2, %(image2), gamma)
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# Make the background transparent using roi
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Greying out the python logo (creating a mask of the logo)
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # convert the color
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# if pixel value is above 220, it'll be converted to 255

cv2.imshow('image2gray', img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()