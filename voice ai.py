
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id) 
engine.setProperty('voice', voices[1].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour >=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak(" the formula for a quadractic equation is minus b , minus or plus the square root of 2b minus 4ac divided by 2a ")
    print("-b-/+ (root of)2b-4ac/2")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
     print(e)
     print("Say that again")
     return "None"
    return query     


if __name__ == "__main__":
    wishMe()
    while True:
     query = takeCommand().lower()

# Logic for executing task based on query 
