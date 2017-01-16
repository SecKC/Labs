from ubidots import ApiClient
import RPi.GPIO as GPIO
import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
device = led.matrix(cascaded=2)

time.sleep(.2)
#Required to set oritation correctly
device.show_message(" ")
for angle in [0, 90, 180, 270]:
   device.orientation(angle)
   #sets brightness 1-10
   device.brightness(2)
   time.sleep(.1)


try:
    api = ApiClient(token='')
    SecKCers = api.get_variable('')

except:
    print "Error: 23 - I can't counter hackers. Check your internets"
    counter = 0
    peoplev = 0

while(1):

    presence = GPIO.input(7)

if(presence):
    hackercount += 1
    presence = 0
    time.sleep(1.5)
    time.sleep(1)
    counter += 1

if(counter == 1):
    print hackercount
    device.show_message(hackercount[''].encode('utf-8'))
    SecKCers.save_value({'value': hackercount})
    counter = 0
    peoplev = 0
