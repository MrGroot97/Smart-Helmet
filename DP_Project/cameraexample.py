import picamera
import time
import pyrebase
import os

config = {
    "apiKey": "AIzaSyBuEOc4pS2628UVtv6CKNWhkOzoR9Z52mQ",
    "authDomain": "testing-e5641.firebaseapp.com",
    "databaseURL": "https://testing-e5641.firebaseio.com",
    "projectId": "testing-e5641",
    "storageBucket": "testing-e5641.appspot.com",
    "messagingSenderId": "629027196086",

}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
camera= picamera.PiCamera()
string =[ "photo"+str(i) for i in range(6)]

#camera.vflip = True 
for i in range(1,6):
    camera.capture('/home/pi/Desktop/Picam/'+string[i]+'.jpg')
    time.sleep(1)
    print(i)
#camera.hflip = True



for i in range(1,6):
    print(string[i])
    storage.child('/Picam/'+string[i]+'.jpg').put('/home/pi/Desktop/Picam/'+string[i]+'.jpg')

