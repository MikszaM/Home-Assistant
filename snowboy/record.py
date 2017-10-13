# -*- coding: utf-8-*-

import pyaudio as pya
import wave
import os
import snowboydecoder

def start():
    FORMAT = pya.paInt16
    CHANNELS = 2
    RATE = 48000
    CHUNK = 2048
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "temp.wav"
    os.system('aplay resources/ding.wav')    
    audio = pya.PyAudio()
         
        # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    print "recording..."
    frames = []
         
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"
         
     
        # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
         
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
