

This uses deepfaces and opencv as a method for authenticating users using facial recognition.

Store saved users in users.json

Store saved users faces in faces directory

Users must be unique

When attempting to login, if user found in users.json, will compare webcam to saved image for that user

CONTROLS

space= take no picture

s = save most recent photo to faces

esc = exit program cleanly (deletes most recent capture)

The goal at the moment it to integrate this into my Arch linux login proccess.

REQUIRED PYTHON PACKAGES:

deepfaces           # for facial_recognition handling

tf-keras            # Fixes issue with deepfaces

opencv-python       # For webcam usage and iamge handling

os                  #for file handling

json                # form json handling
