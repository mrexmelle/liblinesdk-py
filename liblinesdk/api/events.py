# coding: utf-8

import json
import requests
import urllib
from ..enums import ContentType, UserType

def send_message(channel_token, to, content):
    h={'X-Line-ChannelToken': channel_token, 'Content-Type': 'application/json; charset=UTF-8'}
    d={'to':to, 'toChannel':1383378250, 'eventType':'138311608800106203', 'content': content}
    print 'data: ', d
    r=requests.post('https://api.line.me/v1/events', headers=h, data=json.dumps(d))
    print 'status code: ', r.status_code
    print 'headers: ', r.headers
    print 'content: ', r.content

def send_text_message(channel_token, to, to_type, text):
    content={'contentType': ContentType.text, 'toType': to_type, 'text': text}
    send_message(channel_token, to, content)

def send_image_message(channel_token, to, to_type, original_content_url, preview_image_url):
    content={'contentType': ContentType.image, 'toType': to_type,
        'originalContentUrl': original_content_url, 'previewImageUrl': preview_image_url}
    return send_message(channel_token, to, content)

def send_video_message(channel_token, to, to_type, original_content_url, preview_image_url):
    content={'contentType': ContentType.video, 'toType': to_type,
        'originalContentUrl': original_content_url, 'previewImageUrl': preview_image_url}
    return send_message(channel_token, to, content)

def send_audio_message(channel_token, to, to_type, original_content_url, audio_length):
    metadata={'AUDLEN': audio_length}
    content={'contentType': ContentType.audio, 'toType': to_type,
        'originalContentUrl': original_content_url, 'contentMetadata': metadata}
    return send_message(channel_token, to, content)

def send_location_message(channel_token, to, to_type, title, latitude, longitude):
    location={'title': title, 'latitude': latitude, 'longitude': longitude}
    content={'contentType': ContentType.location, 'toType': to_type, 'text': title, 'location': location}
    return send_message(channel_token, to, content)

def send_sticker_message(channel_token, to, to_type, sticker_id, sticker_package_id):
    metadata={'STKID': sticker_id, 'STKPKGID': sticker_package_id}
    content={'contentType': ContentType.sticker, 'toType': to_type, 'contentMetadata': metadata}
    return send_message(channel_token, to, content)
