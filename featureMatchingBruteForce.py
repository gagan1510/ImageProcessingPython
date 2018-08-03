import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('GF1.jpg', 0)
img2 = cv2.imread('GF2.jpg', 0)

# ORB is intended to be rotation invariant and deals well with noise, while being much faster than other feature detectors of the past ages.
# this detects if a point on the image is a feature or not.
# The accuracy doesn't change significantly with the change in color
orb = cv2.ORB_create()
#this is the detector of similarities

# defining and initializing the key points and the descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Brute Force Matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# Match the features and find the ones which are similiar (BruteForce)
matches = bf.match(des1, des2)
# we sort them on the basis of confidence of the similarities found
matches = sorted(matches, key = lambda x:x.distance)

# show the matches in an image and specifying the number of matches from img1 and img2
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:100], None, flags = 2)
plt.imshow(img3)
plt.show()