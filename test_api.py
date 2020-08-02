import cv2, os
from time import sleep
# from script import get_audio, assistant_speaks
from google.cloud import vision
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
import subprocess
from googletrans import Translator
trans= Translator()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="thi.json"
client = vision.ImageAnnotatorClient()
num = 0
def assistant_speaks(output): 
	global num 
  
	# num to rename every audio file  
	# with different name to remove ambiguity 
	num += 1
	print("PerSon : ", output) 
  
	toSpeak = gTTS(text = output, lang ='vi', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3"  
	toSpeak.save(file) 
	  
	# playsound package is used to play the same file. 
	playsound.playsound(file, True)  
	os.remove(file) 
  
  
  
def get_audio(): 
  
	rObject = sr.Recognizer() 
	audio = '' 
  
	with sr.Microphone() as source: 
		print("Speak...") 
		  
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5)  
	print("Stop.") # limit 5 secs 
  
	try: 
  
		text = rObject.recognize_google(audio, language ='vi-VN') 
		print("You : ", text) 
		return text 
  
	except: 
  
		assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0

def takephoto():
	
# initialize the camera
	cam = cv2.VideoCapture(0)
	ret, image = cam.read()

	if ret:
	#cv2.imshow('SnapshotTest',image)
	#cv2.waitKey(0)
	#cv2.destroyWindow('SnapshotTest')
		cv2.imwrite('image.jpg',image)
	cam.release()

def obj_detect():
	takephoto() # First take a picture
	"""Run a label request on a single image"""

	with open('image.jpg', 'rb') as image_file:
		content = image_file.read()

	image = vision.types.Image(content=content)

	# response = client.logo_detection(image=image)


	response = client.label_detection(image=image)
	labels = response.label_annotations
	print('Labels:')

	for label in labels:
		sleep(4)
		# y = labels.description
		translations = trans.translate(label.description,src= "vi", dest='en')
		# os.popen( 'espeak "{}" --stdout | aplay 2>/dev/null'.format(label.description))
		print(label.description)
	return translations
def tim():
	assistant_speaks("bạn muốn tìm đồ vật nào")
	dovat = get_audio()
	y = obj_detect()
	print(y)
	for label in y:
		if str(dovat) in str(y):
			print("đồ bạn tìm hướng này nè")
		else:
			print("tim hương khác đi")


if __name__ == '__main__':
	# try:
	#     main()
	# except:
	#     print('Loi Network')
	tim()






	# i=1
	# while i==1:
	# 	y = tim()
	# 	if (y==0):
	# 		continue
	# 	if (y==1):
	# 		break