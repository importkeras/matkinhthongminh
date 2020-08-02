import argparse
import io

from google.cloud import vision
from google.cloud.vision import types
import os
def takephoto():
    
# initialize the camera
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()

    if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
        cv2.imwrite('/home/pi/huy.jpg',image)
    cam.release()
def canh(image_file):
    takephoto()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Desktop/MATKINHTHONGMINH/huy.json"
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open('home/pi/huy.jpg', 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.landmark_detection(image=image)
    labels = response.landmark_annotations
    for label in labels:
        print('Found landmark: {}'.format(label.description))
    return label.description
os.popen( 'espeak "{}" --stdout | aplay 2>/dev/null'.format(label.description))
# path= 'D:/rong.jpg'
# result=canh(path)
# print(result)
# /home/pi/Desktop/MATKINHTHONGMINH/