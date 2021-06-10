#IMporting OpenCV
import cv2
import numpy

#reading images
photo1=cv2.imread("female.jpg")
male=cv2.imread("male.jpg")

#Resizing to merge
photo2=cv2.resize(male, (564,824))

#Merging and showing
cv2.imshow("hi",numpy.hstack((photo1, photo2)))
cv2.waitKey()
cv2.destroyAllWindows()
