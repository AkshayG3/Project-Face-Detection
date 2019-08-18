# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:51:54 2019

@author: Akshay
"""

import cv2

video = cv2.VideoCapture(0)


#creating a cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
a = 1

while True :
    a =+ 1
    check , frame = video.read()
    print(frame)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #search the coordinate of the image
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.05,minNeighbors=5)

    for x,y,w,h in faces:
        img = cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)
    
    cv2.imshow("VideoCapturing",img)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
print(a)
video.release()
cv2.destroyAllWindows()