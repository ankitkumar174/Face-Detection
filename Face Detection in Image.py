import cv2 as cv
import numpy as np
img = cv.imread("C:\\Users\\ankit\\Documents\\Project Files\\Face detection 3.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier(r"C:\Users\ankit\Documents\Python Scripts\haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
print(f'Number of faces found = {len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Detected Faces",img)
cv.waitKey(0)
