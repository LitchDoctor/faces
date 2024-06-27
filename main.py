import cv2
from deepface import DeepFace
import json
import os
import numpy as np
import imutils

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def list_default(obj):
    if isinstance(obj, list):
        return set(obj)
    raise TypeError

file = open("users.json")

users = json.load(file)

old = None

name = input("What is your username: ")
if (name in users):
    print("Welcome Back. PLease Verify")
    old = cv2.imread("faces/"+name+".jpg")
else:
    print("Welcome New User. PLease Surrender Your Likeness")

camera = cv2.VideoCapture(0)  # Defines Camera 
cv2.namedWindow("Camera Feed")


while True:
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        break
    if os.path.exists("capture.jpg"):
        capture = cv2.imread("capture.jpg")
        cv2.imshow('HORIZONTAL', np.concatenate((frame, capture), axis=1))
    else:
        if old is not None:
            cv2.imshow('HORIZONTAL', np.concatenate((frame, old), axis=1))
        else:
            cv2.imshow("Camera Feed", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "capture.jpg"
        if os.path.exists("demofile.txt"):
            os.remove("capture.jpg")
        cv2.imwrite(img_name, frame)
    elif k%256 == 118:
        if (old is not None) and (os.path.exists("capture.jpg")):
            try:
                result = DeepFace.verify(img1_path = "capture.jpg", img2_path = "faces/"+name+".jpg")
                print(result["verified"])
            except Exception as error:
                print("False: Error")
        else:
            print("Either capture or old does not exist")
    elif k%256 == 115:
        # S pressed
        if os.path.exists("capture.jpg"):
            os.rename("capture.jpg", "faces/"+name+".jpg")
            break
        else:
            print("There is nothing to save")
camera.release()

cv2.destroyAllWindows()
if os.path.exists("capture.jpg"):
    os.remove("capture.jpg")
