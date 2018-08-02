import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('onePillow.jpg', 0)
img2 = cv2.imread('multiplePillows.jpg', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
