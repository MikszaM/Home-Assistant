# -*- coding: utf-8-*-
import os
from time import gmtime, strftime
import speak

class Radio():       
    def set_on_hits(self):
	os.system('radioonhits')
    def set_off(self):
	os.system('radiooff')

class Light():
    def set_on(self):
        os.system('python /home/pi/swiatlo/wlacz2.py')
    def set_off(self):
        os.system('python /home/pi/swiatlo/wylacz2.py')
class Hour():
    def tell(self):
        now= strftime("%H %M")
        speak.say("Jest godzina %s" % now)
class Any():
    def dong(self):
        os.system('aplay /home/pi/snowboy/dong.wav')