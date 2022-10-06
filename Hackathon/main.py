import numpy as np
import cv2
import os

cascPathface = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
casceyeface = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_eye.xml"
cascmouthface = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_mcs_mouth.xml"

#load the xml files for face, eye and mouth detection into the program
face_cascade=cv2.CascadeClassifier(cascPathface)

eye_cascade = cv2.CascadeClassifier(casceyeface)
mouth_cascade = cv2.CascadeClassifier(cascmouthface)

#read the image for furthur editing
image = cv2.imread('img.png')

#show the original image
cv2.imshow('Original image', image)
cv2.waitKey(100)

#convert the RBG image to gray scale image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#identify the face using haar-based classifiers

faces = face_cascade.detectMultiScale(gray_image, 1.4, 4)
# print(faces)
# faces = face_cascade.detectMultiScale(gray_image,
#                                          scaleFactor=1.4,
#                                          minNeighbors=4,
#                                          minSize=(60, 60),
#                                          flags=cv2.CASCADE_SCALE_IMAGE)

#iteration through the faces array and draw a rectangle

for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]


 #identify the eyes and mouth using haar-based classifiers
eyes = eye_cascade.detectMultiScale(gray_image, 1.3, 5)
# eyes1 = eye_cascade.detectMultiScale(gray_image,
#                                      scaleFactor=1.3,
#                                      minNeighbors=5)
                                     # minSize=(60, 60),
                                     # flags=cv2.CASCADE_SCALE_IMAGE)
# print(eyes ,"eyes")
print(eyes ,"eyes")
mouth = mouth_cascade.detectMultiScale(gray_image, 1.3, 11)
print(mouth,"mouth")
# mouth = mouth_cascade.detectMultiScale(gray_image,
#                                          scaleFactor=1.5,
#                                          minNeighbors=11)
#                                          minSize=(60, 60),
#                                          flags=cv2.CASCADE_SCALE_IMAGE)
#iteration through the eyes and mouth array and draw a rectangl
for(ex, ey, ew, eh) in eyes:
    cv2.rectangle(image,(ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    # roi_gray = gray_image[ey:ey + eh, ex:ex + ew]
    # roi_color = image[ey:ey + eh, ex:ex + ew]
for(mx, my, mw, mh) in mouth:
    cv2.rectangle(image, (mx, my), (mx+mw, my+mh), (255, 0, 0), 2)
#     roi_gray = gray_image[my:my + mh, mx:mx + mw]
#     roi_color = image[my:my + mh, mx:mx + mw]



#show the final image after detection
cv2.imshow('face, eyes and mouth detected image', image)
cv2.waitKey()


#show a successful message to the user
print("Face, eye and mouth detection is successful")























































