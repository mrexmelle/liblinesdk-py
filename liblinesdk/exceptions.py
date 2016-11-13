# coding: utf-8

import json

class LineException(Exception):
    code=0
    message=''
    
    def __init__(self, code, message):
        self.code=code
        self.message=message

    @staticmethod
    def from_dictionary(dict):
        return LineException(
            int(dict['error']),
            dict['error_desciption'])

    @staticmethod
    def from_string(string):
        js=json.loads(string)
        return LineException.from_dictionary(js)
