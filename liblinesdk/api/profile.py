# coding: utf-8

import json
import requests
from ..models import Profile
from ..exceptions import LineException

def get(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    r=requests.get('https://api.line.me/v1/profile', headers=h)
#    print 'status code: ', r.status_code
#    print 'headers: ', r.headers
#    print 'content: ', r.content
    if r.status_code == 200:
        return Profile.from_string(r.content)
    else:
        raise LineException.from_string(r.content)
