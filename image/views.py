from django.shortcuts import render
from home.models import Article
from home.forms import UploadImage

import cv2
import numpy as np

import urllib
from django.contrib.staticfiles.templatetags.staticfiles import static




def index(request):

    img_url = '/images/' + str(request.FILES["image"])
    upload = UploadImage(request.POST or None, request.FILES or None)
    instance = upload.save()
    instance.save()

    return render(request, 'image.html', {'img_url': img_url})

def changed(request):
    img_url = str(Article.objects.last())
    afbeelding = img_url.split('/')
    img_url = afbeelding[-2] + '/' + afbeelding[-1]

    TIJDELIJK = 'http://127.0.0.1:8000'

    volle_url = static(img_url)
    volle_url = TIJDELIJK + volle_url

    def drawBoundry(img, classifier, scaleFactor, minNeighbors, color, text):
        features = classifier.detectMultiScale(img, scaleFactor, minNeighbors)
        coords = []
        # drawing rectangle around the feature and labeling it
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
            coords = [x, y, w, h]
        return coords

    def faceDetection(gray, faceClass):
        color = {"blue": (255, 0, 0)}
        coords = drawBoundry(gray, faceClass, 1.1, 10, color['blue'], "Face")
        return gray

    faceDetect = cv2.CascadeClassifier('C:/Users/makin/Prijsvoorspelling/image/haarcascade_frontalface_default.xml')
    if faceDetect.empty():
        print('shit isnt working')

    req = urllib.request.urlopen(volle_url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)  # 'Load it as it is'

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = faceDetection(gray, faceDetect)
    cv2.imwrite('C:/Users/makin/Prijsvoorspelling/static/images/facerec.jpg',img)
    img_url = '/images/facerec.jpg'

    return render(request, 'go.html', {'img_url': img_url})