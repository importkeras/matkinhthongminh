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
def detect_faces(path):
    """Detects faces in an image."""
    takephoto()
    from google.cloud import vision
    import io
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:/huy.json"
    client = vision.ImageAnnotatorClient()
    with io.open('/home/pi/huy.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        # print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        # print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        # print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in face.bounding_poly.vertices])

        # print('face bounds: {}'.format(','.join(vertices)))
        if likelihood_name[face.joy_likelihood] == "LIKELY" or likelihood_name[face.joy_likelihood] == "VERY_LIKELY":
            result ='vui vẻ'
        elif likelihood_name[face.anger_likelihood] == "LIKELY" or likelihood_name[face.anger_likelihood] == "VERY_LIKELY":
            result='bực bội'
        elif likelihood_name[face.anger_likelihood] == "LIKELY" or likelihood_name[face.anger_likelihood] == "VERY_LIKELY":
            result='ngạc nhiên'
        else :
            result='không cảm xúc'

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return result
os.popen( 'espeak "{}" --stdout | aplay 2>/dev/null'.format(result))
# path = 'D:/atan.jpg'
# kq = detect_faces(path)
# print(kq)