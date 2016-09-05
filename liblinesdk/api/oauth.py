# coding: utf-8

import requests
import urllib

def logout(access_token):
    h={'Authorization': 'Bearer ' + access_token}
    r=requests.delete('https://api.line.me/v1/oauth/logout', headers=h)
    print 'status code: ', r.status_code
    print 'headers: ', r.headers
    print 'content: ', r.content

def reissue(refresh_token, channel_secret):
    h={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/x-www-form-urlencoded'}
    d={'refreshToken': refresh_token, 'channelSecret': channel_secret}
    r=requests.post('https://api.line.me/v1/oauth/accessToken', headers=h, data=urllib.urlencode(d))
    print 'status code: ', r.status_code
    print 'headers: ', r.headers
    print 'content: ', r.content
