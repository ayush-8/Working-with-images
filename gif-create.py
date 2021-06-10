import cv2
import numpy
photo = numpy.zeros((500,500,3))

photo[ 85:-85, 151:157]  = [255,255,255]
photo[ 85:-85, -157:-151]= [255,255,255]
photo[-86:-80, 151:-151] = [255,255,255]
photo[ 80:86 , 151:-151] = [255,255,255]
photo[ 70:80 , 225:-225] = [255,255,255]

while True:
    photo[-410:-90 , 160:-160] = [0,0,0]
    cv2.imshow("Task 4.1", photo)
    if cv2.waitKey(1500) == 13:
        break
    photo[-154:-90 , 160:-160] = [0,0,255]
    cv2.imshow("Task 4.1", photo)
    if cv2.waitKey(1500) == 13:
        break
    photo[-218:-90, 160:-160] = [0,255,255]
    cv2.imshow("Task 4.1", photo)
    if cv2.waitKey(1500) == 13:
        break
    photo[-282:-90, 160:-160] = [0,255,255]
    cv2.imshow("Task 4.1", photo)
    if cv2.waitKey(1500) == 13:
        break
    photo[-346:-90, 160:-160] = [0,255,0]
    cv2.imshow("Task 4.1", photo)
    if cv2.waitKey(1500) == 13:
        break
    photo[-410:-90, 160:-160] = [0,255,0]
    cv2.imshow("Task 4.1", photo)
    if cv2.waitKey(1000) == 13:
        break
cv2.destroyAllWindows()
