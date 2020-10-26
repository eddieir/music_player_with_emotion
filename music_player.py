import time
import cv2
import label_image
import os,random
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
size = 4

# let's load the xml
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
global text
webcame = cv2.VideoCapture(0)
now = time.time()
future = now + 60
while True:
    (rval,im) = webcame.read()
    im = cv2.flip(im,1,0)
    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    faces = classifier.detectMultiScale(mini)

    # Draw rectangle around each face

