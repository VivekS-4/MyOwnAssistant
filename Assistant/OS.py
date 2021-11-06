import os
import speech_recognition as sr
import pyttsx3 as p

engine = p.init()


def say(audio):
    engine.say(audio)
    engine.runAndWait()


def tc():
    r = sr.Recognizer()
    # source: sr.Microphone
    with sr.Microphone() as source:
        print("Listening:")
        say("Listening")
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}")
    except Exception as E:
        print(E)
        say("Please say that again..!")
        return "None"
    return query.lower()


say("What's the command?")
qry = tc().lower()
if "logout" in qry:
    os.system("shutdown -l")
elif "shutdown" in qry:
    os.system("shutdown /s /t 1")
elif "restart" in qry:
    os.system("shutdown -r /t 1")
else:
    say("Wrong Command Input")
