import cv2, os
from time import sleep
from googletrans import Translator

from google.cloud import vision
translator = Translator()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Desktop/MATKINHTHONGMINH/huy.json"
client = vision.ImageAnnotatorClient()


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

def main():
    takephoto() # First take a picture
    """Run a label request on a single image"""

    with open('/home/pi/image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)


    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        sleep(3)
        lab = translator.translate(label,src = 'en',dest = 'vi')
        os.open( 'espeak "{}" --stdout | aplay 2>/dev/null'.format(lab.description))
        print(lab.description)
        print(lab)
if __name__ == '__main__':
    #try:
        main()
   # except:
      #  print('Loi Network')

