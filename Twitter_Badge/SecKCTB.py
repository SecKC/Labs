#!/usr/bin/env python

####################################################################################################
#     _______. _______   ______  __  ___   ______     __          ___      .______        _______. #
#    /       ||   ____| /      ||  |/  /  /      |   |  |        /   \     |   _  \      /       | #
#   |   (----`|  |__   |  ,----'|  '  /  |  ,----'   |  |       /  ^  \    |  |_)  |    |   (----` #
#    \   \    |   __|  |  |     |    <   |  |        |  |      /  /_\  \   |   _  <      \   \     #
#.----)   |   |  |____ |  `----.|  .  \  |  `----.   |  `----./  _____  \  |  |_)  | .----)   |    #
#|_______/    |_______| \______||__|\__\  \______|   |_______/__/     \__\ |______/  |_______/     #
#                                                                                                  #
#                                        _____________________                                     #
#                                       < #Outhouse is Banned >                                    #
#                                        ---------------------                                     #
#                                               \   ^__^                                           #
#                                                \  (oo)\_______                                   #
#                                                   (__)\       )\/\                               #
#                                                       ||----w |         SecKC Twitter Badge 1.0  #                      #
#                                                       ||     ||                    @corykennedy  #
####################################################################################################


# https://github.com/rm-hull/max7219
import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange
# pip or easy_install twython
# https://github.com/ryanmcgrath/twython 
from twython import TwythonStreamer

# Search terms - This should never change from #SecKC and if it does you are BANNED!
TERMS = '#SecKC'


# https://apps.twitter.com & https://dev.twitter.com
APP_KEY = '<YOUR CONSUMER KEY>'
APP_SECRET = '<YOUR CONSUMER SECRET>'
OAUTH_TOKEN = '<YOUR ACCESS TOKEN>'
OAUTH_TOKEN_SECRET = '<YOUR ACCESS TOKEN SECRET>'


# Set the number of cascaded matrix's to the number of 7219 8x8 panels you have. 
#Im using this shield: http://www.waveshare.com/rpi-led-matrix.htm
device = led.matrix(cascaded=2)

time.sleep(.2)
#Required to set oritation correctly
device.show_message(" ")
for angle in [0, 90, 180, 270]:
   device.orientation(angle)
   #sets brightness 1-10
   device.brightness(2)
   time.sleep(.1)

class SecKCStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
#                       print data['text'].encode('utf-8')
                        device.show_message(data['text'].encode('utf-8'))
                        print

try:
    stream = SecKCStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
    device.show_message("BANNED!!!")