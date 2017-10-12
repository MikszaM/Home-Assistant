# -*- coding: utf-8-*-

import logging
import tempfile
import wave
import audioop
import pyaudio
import requests
import json
import os
import modules
from commands import Any
any=Any()

API_KEY = 'Your API Key'

hd = {'Authorization': 'Bearer %s' % API_KEY,
           'accept': 'application/json',
           'Content-type': 'audio/wav'}

audio=pyaudio.PyAudio()    
   
def getScore(data):
    rms = audioop.rms(data, 2)
    score = rms / 3
    return score

def transcribe(f):
    data=f.read()
    r = requests.post('https://api.wit.ai/speech?v=20160526',
                      data=data,
                      headers=hd)
    try:
        r.raise_for_status()
        text = r.json()['_text']
    except requests.exceptions.HTTPError:
        print('Request failed with response: %r',
                              r.text)
        any.dong()
        return []
    except requests.exceptions.RequestException:
        print('Request failed.')
        return []
    except ValueError as e:
        print ('Cannot parse response: %s',
                              e.args[0])
        return []
    except KeyError:
        print ('Cannot parse response.')
        return []
    else:
        transcribed = []
        if text:
            transcribed.append(text.upper())
        print('Transcribed: %r', transcribed)
        modules.search(transcribed)                
    return transcribed
        
def fetchThreshold():

        # TODO: Consolidate variables from the next three functions
    THRESHOLD_MULTIPLIER = 1.25
    RATE = 48000
    CHUNK = 2048

        # number of seconds to allow to establish threshold
    THRESHOLD_TIME = 0.25

        # prepare recording stream
    stream = audio.open(format=pyaudio.paInt16,
                              channels=1,
                              rate=RATE,
                              input=True,
                              frames_per_buffer=CHUNK)

        # stores the audio data
    frames = []

        # stores the lastN score values
    lastN = [i for i in range(20)]

        # calculate the long run average, and thereby the proper threshold
    for i in range(0, int(RATE / CHUNK * THRESHOLD_TIME)):

        data = stream.read(CHUNK)
        frames.append(data)

            # save this data point as a score
        lastN.pop(0)
        lastN.append(getScore(data))
        average = sum(lastN) / len(lastN)

    stream.stop_stream()
    stream.close()

        # this will be the benchmark to cause a disturbance over!
    THRESHOLD = average * THRESHOLD_MULTIPLIER*4
    print THRESHOLD
    return THRESHOLD

 
def listen(THRESHOLD=None, LISTEN=True,
                             MUSIC=False):
        
    RATE = 48000
    CHUNK = 2048
    LISTEN_TIME = 6

        # check if no threshold provided
    if THRESHOLD is None:
        THRESHOLD =fetchThreshold()

    os.system('aplay /home/pi/snowboy/beep_hi.wav')

        # prepare recording stream
    stream = audio.open(format=pyaudio.paInt16,
                              channels=1,
                              rate=RATE,
                              input=True,
                              frames_per_buffer=CHUNK)

    frames = []
        # increasing the range # results in longer pause after command
        # generation
    lastN = [THRESHOLD * 1.2 for i in range(30)]

    for i in range(0, RATE / CHUNK * LISTEN_TIME):

        data = stream.read(CHUNK)
        frames.append(data)
        score = getScore(data)

        lastN.pop(0)
        lastN.append(score)

        average = sum(lastN) / float(len(lastN))

            # TODO: 0.8 should not be a MAGIC NUMBER!
        if average < THRESHOLD * 0.8:
            break

    os.system('aplay /home/pi/snowboy/beep_lo.wav')

        # save the audio data
    stream.stop_stream()
    stream.close()
    
    with tempfile.SpooledTemporaryFile(mode='w+b') as f:
        wav_fp = wave.open(f, 'wb')
        wav_fp.setnchannels(1)
        wav_fp.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
        wav_fp.setframerate(RATE)
        wav_fp.writeframes(''.join(frames))
        wav_fp.close()
        f.seek(0)
        return transcribe(f)
