import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Subodhayam!")

    elif hour >= 12 and hour < 18:
        speak("some sun above ")

    else:
        speak("Get some of that workout!")

    speak("Yo i am Zeera , how may i help ya!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)

        print("Yo wait repeat that..")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rithviks.ryk57@gmail.com','opm>naruto')
    server.sendmail('rithviks.ryk57@gmail.com', to,content)
    server.close() 

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wkipedia' in query:
            speak("I'm a look it up on Wikipedia....")
            query = query.replace("wikepedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Well in wikiepdia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            if 'search on youtube in ' in query:
                speak("What do you want to search")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open chezuba' in query:
            webbrowser.open("chezuba.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open zorro anime' in query:
            webbrowser.open("zoro.to")

        elif 'open slope io' in query:
            webbrowser.open("slope.io")

        elif 'open manga reader' in query:
            webbrowser.open("mangareder.to")

        elif 'open adobe express' in query:
            webbrowser.open("adobeexpress.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Well  we are rocking at {strTime} right now')
        
        elif 'math' or 'mathematics' in query:
            speak("what do you want help with ?Check printed message for list of mathematical functions i know .")
            listmath=["Factors of numbers," 
            " Integers, " 
            "Number-operations ," 
             "Prime-Numbers, "
              "Prime-factors ,"
               "Greatest-common-factor, "
                "lowest-common-multiple ," 
                 "Recurring-decimals ," 
                  "Number-Lines, "
                   'inequalities, '     
                   'Ratios, ' 
                    'Exponents and powers, ' 
                    'Squares-and-square roots ,'
                     ' Time zones,' 
                     'clocks,'
                      'Absolute values,' 
                       'Representing And Solving inequalities,'
                        'Irrational numbers,'
                          'Surds,roots and radicals,' 
                            'scientific notation,' 
                            'Laws of exponents,'  
                             'integer and negative exponents,' 
                              'Number system notation,' 
                              'Direct and inverse proportion,']
            print(listmath)
            if'Factors of numbers'  in query :
                speak()    
            elif'Integers' in query :
                speak()
            elif'Number operations' in query:
                speak()
            elif'Prime numbers' in query:
                speak()
            elif'Greatest common factor' in query :
                speak()
            elif'lowest common multiple' in query:
               speak()
            elif'recurring decimals' in query:
                speak()
            elif'number lines' in query :
                speak()
            elif'inequalities' in query:
                speak()
            elif'ratios' in query:
                speak()
            elif'exponents and powers' in query :
                speak()
            elif'squares' or 'square roots' in query:
                speak()
            elif'Time zones' in query:
                speak()
            elif'clocks' in query :
                speak()
            elif'Absolute values' in query:
               speak()
            elif'solving inequalities' in query:
                speak()
            elif'irrational numbers' in query :
                speak()
            elif'surds' or 'roots' or 'radicals' in query:
                speak()
            elif'scientifc notation' in query:
                speak()
            elif'Laws' in query :
                speak()
            elif'integer and negative exponents' in query:
                speak()
            elif'number system notation' in query:
                speak()
            elif'direct proportion' or 'inverse proportion' in query :
                speak()
            else :
                speak("didnt get u bruh , repeat")
        
        
        elif 'email to ricky'in query:
            try:
                speak('what should i say')
                content=takeCommand()
                to='rithvik.sabnekar@akahyd.org'
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e :
                print('e')
                speak("not able to send man")

        elif 'quit' in query:
         break

