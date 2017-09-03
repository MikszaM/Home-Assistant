import snowboydecoder
import active

detector = snowboydecoder.HotwordDetector("/home/pi/snowboy/sluchaj2.pmdl", sensitivity=0.5, audio_gain=1)

def detected_callback():
    print "hotword detected"
    detector.terminate()
    active.listen()
    start()
    
def start():
    detector.start(detected_callback)