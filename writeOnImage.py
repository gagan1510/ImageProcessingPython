import numpy as np 
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# this function will add a line to the image from (0,0) to (150,150) and the colour is (R,G,B)
cv2.line(img, (0,0), (150, 150), (255, 255, 255), 5)

# add a rectangle to the image (top coordinate, bottom coordinate
cv2.rectangle(img, (15,25), (200,150), (0,0,255), 5)

# add a circle to the image (center, radius, color, radius)
cv2.circle(img, (100,63), 55, (0,0,255), -1)
# (-1) radius is to fill the circle up with the colour

# a polygon can also be drawn using a series or set of points
pts = np.array([[133,22], [13,34], [54,65], [70,80], [90,100]], np.int32)
pts = pts.reshape(((-1,1,2)))
cv2.polylines(img, [pts], True, (0,255,120), 3)

# to write on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Practice!", (0, 30), font, 1, (200,255,255), 2, cv2.LINE_AA)

# show the image until any key is pressed
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()