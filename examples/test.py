# -*- coding: utf-8 -*-

import nfc
import pygame.mixer
import time
import requests
import json

myCardId = '011603004011DA01'

def on_connect(tag):
    tag_id = str(tag)
    if tag_id.find(myCardId) > 0:
        print('weeeeeeeeeeeeeeee')
        play_sound()
        slack_request()
        return True
    else:
        print 'error'
        print tag_id

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('ikusa1.mp3')
    pygame.mixer.music.play(2)
    time.sleep(10)
    pygame.mixer.stop()
    print "volume:%s" % pygame.mixer.music.get_volume()
    print "play time:%s[ms]"%pygame.mixer.music.get_busy()

def slack_request():
    requests.post('https://hooks.slack.com/services/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', data = json.dumps({
        'text': u'皆の者出陣じゃ！',
        'username': u'UK',
        'icon_emoji': u':uesugi_kenshin:',
        'link_names': 1
    }))

if __name__=='__main__':


    clf = nfc.ContactlessFrontend('usb')

    try:
        while True:
                clf.connect(rdwr={'on-connect': on_connect})
                pass
    except KeyboardInterrupt:
        pygame.mixer.quit()
