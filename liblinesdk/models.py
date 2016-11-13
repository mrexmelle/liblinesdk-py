# coding: utf-8

import json

class Profile:
    mid=''
    display_name=''
    picture_url=''
    status_message=''

    def __init__(self, mid, display_name, picture_url, status_message):
        self.mid=mid
        self.display_name=display_name
        self.picture_url=picture_url
        self.status_message=status_message
    
    @staticmethod
    def from_dictionary(dict):
        return Profile(
            dict['mid'],
            dict['displayName'],
            dict['pictureUrl'],
            dict['statusMessage'])
    
    @staticmethod
    def from_string(string):
        js=json.loads(string)
        return Profile.from_dictionary(js)

    def get_small_picture_url(self):
        return self.picture_url + '/small'

    def get_large_picture_url(self):
        return self.picture_url + '/large'

class FriendList:
    count=0
    contacts=[]
