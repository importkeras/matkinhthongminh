from __future__ import print_function
import requests
import json
import cv2
import os
import pygame
from gtts import gTTS
pygame.init()
num=0
import cv2

# initialize the camera
cam = cv2.VideoCapture(0)
ret, image = cam.read()

if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/Desktop/MATKINHTHONGMINH/test.jpg',image)
cam.release()
def assistant_speaks(output): 
    global num 
  
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = str(num)+".mp3 " 
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    os.remove(file)
addr = 'http://34.87.28.196:80'
test_url = addr + '/uploads'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('test.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
#print(json.loads(response.text))
print(response.text)
assistant_speaks(response.text)

# expected output: {u'message': u'image received. size=124x124'}