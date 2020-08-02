from time import sleep
import subprocess
#from gtts import gTTS
#from googletrans import Translator
#import pygame
stt=3
time=2

file1="/home/pi/Desktop/MATKINHTHONGMINH/label.py"
file2="/home/pi/Desktop/MATKINHTHONGMINH/ocr.py"
file3="/home/pi/Desktop/MATKINHTHONGMINH/vnt.py"
while True:
    try:
        sleep(time)
        if stt==0:
            break
        if stt==1:
            subprocess.run("python3 {}".format(file1),shell=True)
        if stt==2:
            subprocess.run("python3 {}".format(file2),shell=True)
        if stt==3:
            subprocess.run("python3 {}".format(file3),shell=True)
    except:
        print('Loi network')
    
