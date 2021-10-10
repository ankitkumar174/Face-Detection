import cv2 as cv
import numpy as np
haar_cascade = cv.CascadeClassifier(r"C:\Users\ankit\Documents\Python Scripts\haar_face.xml")
camera=cv.VideoCapture(0)
while True:
    check,frame=camera.read()
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for(x,y,w,h) in faces_rect:
        frame=cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow("Detected Faces",frame)
    key=cv.waitKey(1)
    if key == ord('q'):
        break
camera.release()
cv.destroyAllWindows()
print(f'Number of faces found = {len(faces_rect)}')