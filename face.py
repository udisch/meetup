import requests
import sys

if len(sys.argv) < 2:
    print "usage: %s image_url" % sys.argv[0]
    sys.exit(1)

url = 'https://api.projectoxford.ai/face/v1.0/detect?'
face_attributes = 'age,gender'
api_key = 'put_api_key_here'

image_url = sys.argv[1]
payload = {'url': image_url}

resp = requests.post(url, params = {'returnFaceAttributes': face_attributes, 'returnFaceLandmarks': 'false', 'returnFaceId': 'false'}, headers = {'Ocp-Apim-Subscription-Key': api_key, 'Content-Type': 'application/json'}, json=payload)
if (resp.status_code == 200):
    json = resp.json()
    if len(json) > 0:
        attributes = resp.json()[0]['faceAttributes']
        print 'gender: %s, age: %s' % (attributes['gender'], attributes['age'])
    else:
        print 'no face detected'
else:
    print resp.status_code
