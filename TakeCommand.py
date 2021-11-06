import speech_recognition as sr #pip install SpeechRecognition
import pyttsx3 as p #pip install pytysx3

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

tc()
