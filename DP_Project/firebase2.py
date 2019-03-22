import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

image_url = '/home/pi/Desktop/photo1.jpg' #we pass the url as an argument

cred = credentials.Certificate('/home/pi/Desktop/firebase/firebaseauth.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'smart-helmet-2aa6d.appspot.com'
})
bucket = storage.bucket()

image_data = requests.get(image_url).content
blob = bucket.blob('new_cool_image.jpg')
blob.upload_from_string(
        image_data,
        content_type='image/jpg'
    )
print(blob.public_url)
