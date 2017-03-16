__author__ = 'ilanzaitoun'
import json
import requests

url = 'http://localhost:3000/upload'
headers = {}
image_metadata = {}
PATH = 'sample_files/aa1.png'
FILE='1.png'
data = {'name': 'image.jpg', 'data': json.dumps(image_metadata)}
files = {'file': (FILE, open(PATH, 'rb'), 'image/jpg', {'Expires': '0'})}
r = requests.post(url, files=files, headers=headers, data=data)

print r

