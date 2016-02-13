[![Badge Jiff](https://raw.githubusercontent.com/SecKC/seckc.github.io/master/images/badges/SecKC_Twitter_Badge.gif)](https://youtu.be/bD3Shz_lzPA)



SecKC Twitter Badge
========================
![SecKC](https://raw.githubusercontent.com/SecKC/seckc.github.io/master/images/logo/SecKC_Hex_OnlyB_small.png "SecKC")
## Requirements ##
### Hardware ###
* Raspberry Pi (Any Model)
* http://www.waveshare.com/rpi-led-matrix.htm <-- (2)8x8 7219 LED matrcies for a total of 8 x 16 in a shield for the pi.

### Software ###
* https://github.com/rm-hull/max7219
* https://github.com/ryanmcgrath/twython 
* Internet connection to monitor twitter for #SecKC
* SPI interface enabled https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md or just do it from raspi-config
* Read https://dev.twitter.com/faq section on API

### How to use ###
```
 git clone https://github.com/SecKC/Labs.git
```
* Add your Twitter authorization APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET to SecKCTB.py
* Ban someone
* Execute script via CLI instructions below
* Join #outhouse over at seckc.slack.com
* Start tweeting about #SecKC and marvel at your hacking skills

### Using CLI ###

Sudo is required to interface with SPI
```
$ sudo python SecKCTB.py
```
Add to /etc/rc.local. I couldnt get this to work without adding sudo

```
(sleep 10;python sudo /path/SecKCTB.py)&
````

## How it Works
More to come

## More Info
* http://raspi.tv/2013/8-x-8-led-array-driven-by-max7219-on-the-raspberry-pi-via-python
* http://soundcloud.com/mau5trap
* http://SecKC.org
* http://blog.eikeland.se/2014/04/21/max7219-rpi-clojure/ 
* https://apps.twitter.com
