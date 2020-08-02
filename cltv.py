import cv2, os
from time import sleep

from googletrans import Translator
from google.cloud import vision
translate= Translator()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Desktop/MATKINHTHONGMINH/huy.json"
client = vision.ImageAnnotatorClient()
num=0
def translate_cap(caption):
    translator= Translator()
    sent= translator.translate(caption, dest='vi',src ='en')
    return sent.text
def takephoto():
    
# initialize the camera
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()

    if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
        cv2.imwrite('/home/pi/image.jpg',image)
    cam.release()
def assistant_speaks(output): 
    global num 
  
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num =+1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = 'ai.mp3' 
    toSpeak.save(file)
    os.system("mpg321 -q ai.mp3")
def main():
    takephoto() # First take a picture
    """Run a label request on a single image"""

    with open('/home/pi/image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)


    response = client.label_detection(image=image)
    labels = response.label_annotations
    trans = translate_cap(labels)
    print('Labels:')
    sleep(2)
    print(trans)
    assistant_speaks(trans)

if __name__ == '__main__':
  main()