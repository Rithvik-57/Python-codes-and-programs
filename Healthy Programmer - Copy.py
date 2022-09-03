#Healthy programmer - water , eyes and physical activty reminder

from pygame import mixer 
import time 
import datetime

def getdate() :
    return datetime.datetime.now

def playmusic(file , stopper) :
    mixer.init()
    mixer.music.load(file) 
    mixer.music.play()
    while True :
        a = input()
        if a==stopper:
            mixer.music.stop()
            break
if __name__=='__main__':
    playmusic(" waterrem.mp3 ", "stop")

     

