#IMporting OpenCV
import cv2

#reading images
photo1=cv2.imread("female.jpg")
male=cv2.imread("male.jpg")

#Resizing to get the same size of both images
photo2=cv2.resize(male, (int(male.shape[1] * 0.36), int(male.shape[0] * 0.36)))   
cv2.imshow("hi",photo1)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("hi",photo2)
cv2.waitKey()
cv2.destroyAllWindows()

#Loading the face detection model
model=cv2.CascadeClassifier("../ML/haarcascade_frontalface_default.xml")
# Detecting faces
face1=model.detectMultiScale(photo1)
face2=model.detectMultiScale(photo2)

# enclosing detected faces in rectangles

rphoto2=cv2.rectangle(photo2, (face2[0][0],face2[0][1] ), (face2[0][0] + face2[0][2] ,face2[0][1]+ face2[0][3]), (0,255,0), 3)
rphoto1=cv2.rectangle(photo1, (face1[0][0],face1[0][1] ), (face1[0][0] + face1[0][2] ,face1[0][1]+ face1[0][3]), (0,255,0), 3)

#Creating copies to swap
cphoto1=rphoto1.copy()
cphoto2=rphoto2.copy()

# Cropping the images from copies

crop1=cphoto1[face1[0][1] :face1[0][1]+ face1[0][3],face1[0][0] :face1[0][0] + face1[0][2]]
crop2=cphoto2[face2[0][1] :face2[0][1]+ face2[0][3],face2[0][0] :face2[0][0] + face2[0][2]]

# Swapping in the original photos the cropped part

rphoto2[face2[0][1] :face2[0][1]+ face2[0][3],face2[0][0] :face2[0][0] + face2[0][2]]=cv2.resize(crop1, (381,381))
rphoto1[face1[0][1] :face1[0][1]+ 381,face1[0][0] :face1[0][0] + 381]=crop2
#Finally Viewing the photos

cv2.imshow("hi",rphoto1)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("hi",rphoto2)
cv2.waitKey()
cv2.destroyAllWindows()
