# -*- coding: utf-8-*-
import os
import datetime
import speak
import natural
import requests

class Radio():       
    def set_on_hits(self):
	os.system('radioonhits')
    def set_off(self):
	os.system('radiooff')

class Light():
    def set1_on(self):
        os.system('python /home/pi/swiatlo/wlacz1.py')
    def set1_off(self):
        os.system('python /home/pi/swiatlo/wylacz1.py')
    def set3_on(self):
        os.system('python /home/pi/swiatlo/wlacz3.py')
    def set3_off(self):
        os.system('python /home/pi/swiatlo/wylacz3.py')
    def gora(self):
        os.system('python /home/pi/swiatlo/gora.py')
class Hour():
    def tell(self):
        now= datetime.datetime.now()
        message=natural.time(now.hour,now.minute)
        speak.say("Jest godzina %s" % message)
class Date():
    def tell(self):
        now = datetime.datetime.now()
        message=natural.date(datetime.datetime.today().weekday(),now.day,now.month,now.year)
        speak.say("Dzisiaj jest %s" % message)
class Weather():
    def now(self):
        data=requests.get('http://api.wunderground.com/api/c19b901616e46ec2/conditions/lang:PL/q/pws:ICIESZYN3.json').json()
        state=data['weather']
        print state
    #def today(self):
        
   # def tomorrow(self):
        
   # def day(self):
        
class Any():
    def dong(self):
        os.system('aplay /home/pi/snowboy/dong.wav')