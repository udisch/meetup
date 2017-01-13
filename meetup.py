import requests

#resp = requests.get('https://api.meetup.com/<group>/events/<eventid>/rsvps')

for member in resp.json():
    try:
        print "%s %s" % (member['member']['photo']['photo_link'], member['member']['name'])
    except KeyError:
        pass
