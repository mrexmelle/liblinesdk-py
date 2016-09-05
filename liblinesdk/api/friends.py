# coding: utf-8

import requests
import urllib

def get_all(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    r=requests.get('https://api.line.me/v1/friends', headers=h)
    print 'status code: ', r.status_code
    print 'headers: ', r.headers
    print 'content: ', r.content

def get_ingame(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    r=requests.get('https://api.line.me/v1/friends/channel', headers=h)
    print 'status code: ', r.status_code
    print 'headers: ', r.headers
    print 'content: ', r.content
