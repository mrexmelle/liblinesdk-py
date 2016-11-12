# coding: utf-8

import requests

def get(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    r=requests.get('https://api.line.me/v1/permissions', headers=h)
    print 'status code: ', r.status_code
    print 'headers: ', r.headers
    print 'content: ', r.content
