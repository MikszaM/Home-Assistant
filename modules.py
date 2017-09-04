# -*- coding: utf-8-*-
import re
from commands import Light, Radio, Any, Hour

light=Light()
radio=Radio()
any=Any()
hour=Hour()

def search(texts):
    for text in texts:
        if bool(re.search(ur'\bw\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) and bool(re.search(ur'\b\u015Awiat\u0141\w\b',text,re.IGNORECASE | re.UNICODE)):
            light.set_on()
        elif bool(re.search(ur'\bwy\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) and bool(re.search(ur'\b\u015Awiat\u0141\w\b',text,re.IGNORECASE | re.UNICODE)):
            light.set_off()
        elif bool(re.search(ur'\bw\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) and bool(re.search(ur'\bradio\b',text,re.IGNORECASE | re.UNICODE)):
            radio.set_on_hits()
        elif bool(re.search(ur'\bwy\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) and bool(re.search(ur'\bradio\b',text,re.IGNORECASE | re.UNICODE)):
            radio.set_off()
        elif bool(re.search(ur'\bkt\xd3ra\b', text, re.IGNORECASE|re.UNICODE)):
            hour.tell()        
        else:
            any.dong()