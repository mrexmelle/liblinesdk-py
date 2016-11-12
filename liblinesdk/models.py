# coding: utf-8

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

    def get_small_picture_url(self):
        return self.picture_url + '/small'

    def get_large_picture_url(self):
        return self.picture_url + '/large'

class FriendList:
    count=0
    contacts=[]
