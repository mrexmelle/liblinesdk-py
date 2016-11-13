# coding: utf-8

import json
import requests
import urllib
from ..models import FriendList, Profile

def get_all(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    response=FriendList()
    s=1
    while True:
        r=requests.get('https://api.line.me/v1/friends?start=' + str(s) + '&display=100', headers=h)
#        print 'status code: ', r.status_code
#        print 'content: ', r.content
        if r.status_code == 200:
            jr=json.loads(r.content)
            response.count+=jr['count']
            for ctc in jr['contacts']:
                response.contacts.append(Profile.from_dictionary(ctc))
            if jr['count'] < 100:
                break
            else:
                s+=100
        else:
            break
    return response

def get_ingame(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    response=FriendList()
    s=1
    while True:
        r=requests.get('https://api.line.me/v1/friends/channel?start=' + str(s) + '&display=100', headers=h)
#        print 'status code: ', r.status_code
#        print 'content: ', r.content
        if r.status_code == 200:
            jr=json.loads(r.content)
            response.count+=jr['count']
            for ctc in jr['contacts']:
                response.contacts.append(Profile.from_dictionary(ctc))
            if jr['count'] < 100:
                break
            else:
                s+=100
        else:
            break
    return response
