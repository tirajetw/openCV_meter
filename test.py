# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

# load the example image
image = cv2.imread("test.png")
 
# pre-process the image by resizing it, converting it to
# graycale, blurring it, and computing an edge map
image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)