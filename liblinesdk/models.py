# coding: utf-8

class Profile:
    mid=''
    display_name=''
    picture_url=''
    status_message=''

    def get_small_picture_url(self):
        return self.picture_url + '/small'

    def get_large_picture_url(self):
        return self.picture_url + '/large'

class FriendList:
    count=0
    contacts=[]
