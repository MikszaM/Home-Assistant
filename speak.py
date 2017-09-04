# -*- coding: utf-8-*-
import os
from time import gmtime, strftime

def say(text):
    message = 'espeak -vpl -s150 -g3 -p75 -k50 -a150 "%s"' % text
    print message
    os.system(message)
