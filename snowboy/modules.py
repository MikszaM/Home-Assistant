# -*- coding: utf-8-*-
import re
from commands import Light, Radio, Any, Hour, Date

light=Light()
radio=Radio()
any=Any()
hour=Hour()
date=Date()

def search(texts):
    for text in texts:
        if (bool(re.search(ur'\bw\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) or bool(re.search(ur'\bzapal\b', text, re.IGNORECASE | re.UNICODE))) and bool(re.search(ur'\b\u0141\u00d3\u017bk\w\b',text,re.IGNORECASE | re.UNICODE)):
            light.set1_on()
        elif (bool(re.search(ur'\bwy\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) or bool(re.search(ur'\bzga\u015a\b', text, re.IGNORECASE | re.UNICODE))) and bool(re.search(ur'\b\u0141\u00d3\u017bk\w\b',text,re.IGNORECASE | re.UNICODE)):
            light.set1_off()
        elif (bool(re.search(ur'\bw\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) or bool(re.search(ur'\bzapal\b', text, re.IGNORECASE | re.UNICODE))) and (bool(re.search(ur'\bkanap\w\b',text,re.IGNORECASE | re.UNICODE)) or bool(re.search(ur'\bkanapi\w\b',text,re.IGNORECASE | re.UNICODE))):
            light.set3_on()
        elif (bool(re.search(ur'\bwy\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) or bool(re.search(ur'\bzga\u015a\b', text, re.IGNORECASE | re.UNICODE))) and (bool(re.search(ur'\bkanap\w\b',text,re.IGNORECASE | re.UNICODE)) or bool(re.search(ur'\bkanapi\w\b',text,re.IGNORECASE | re.UNICODE))):
            light.set3_off()
        elif bool(re.search(ur'\bg\xd3ra\b', text, re.IGNORECASE|re.UNICODE)) or bool(re.search(ur'\bg\xd3rne\b', text, re.IGNORECASE|re.UNICODE)):
            light.gora()
        elif bool(re.search(ur'\bw\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) and bool(re.search(ur'\bradio\b',text,re.IGNORECASE | re.UNICODE)):
            radio.set_on_hits()
        elif bool(re.search(ur'\bwy\u0141\u0104cz\b', text, re.IGNORECASE | re.UNICODE)) and bool(re.search(ur'\bradio\b',text,re.IGNORECASE | re.UNICODE)):
            radio.set_off()
        elif bool(re.search(ur'\bkt\xd3ra\b', text, re.IGNORECASE|re.UNICODE)):
            hour.tell()
        elif bool(re.search(ur'\bkt\xd3ry\b', text, re.IGNORECASE|re.UNICODE)) and bool(re.search(ur'\bdzisiaj\b', text, re.IGNORECASE|re.UNICODE)):
            date.tell()
        else:
            any.dong()