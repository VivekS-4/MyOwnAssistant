import webbrowser
import pywhatkit
import pyjokes
import datetime
import smtplib
import wikipedia
import speech_recognition as sr
import pyttsx3 as p
import webbrowser as wb
import pyautogui

import psutil

engine = p.init()


def say(audio):
    engine.say(audio)
    engine.runAndWait()


# Speaking time
def time():
    t = datetime.datetime.now().strftime("%I:%M:%S %p")
    say("Current Time is:")
    print(t)
    say(t)


# Speaking Date
def date():
    day = int(datetime.datetime.now().day)
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    say("Today's date is:")
    say(day)
    say(month)
    say(year)


def mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("TestRun@gmail.com", "TestRunPassword")
    #Less Secure apps access should be allowed in the "From" gmail account
    server.sendmail("TestRun@gmail.com", to, content)
    server.close()


def greet():
    engine.setProperty('rate', 250)
    hr = datetime.datetime.now().hour
    if 4 < hr < 12:
        say("Good Morning Sir, Welcome back!")
    elif 12 <= hr < 18:
        say("Good Afternoon Sir, Welcome back!")
    elif 18 <= hr <= 22:
        say("Good Evening Sir, Welcome back!")
    else:
        say("Good Night Sir, Welcome back!")
    # say("How may I help you today?")
    engine.setProperty('rate', 300)
    say("I can Help you with date, time, play a song, wikipedia search, location Search, chrome link open, get a Screenshot, tell you a joke, write down a note for you, CPU usage of the system, and it's battery Percentage.")


def ss():
    img = pyautogui.screenshot()
    img.save("E:/ss.png")


def tc():
    r = sr.Recognizer()
    # source: sr.Microphone
    with sr.Microphone() as source:
        print("Listening:")
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


def cpu():
    usg = str(psutil.cpu_percent())
    say(usg)


def jokes():
    jk = pyjokes.get_joke()
    say(jk)
    print(jk)


def btry():
    prcnt = psutil.sensors_battery()
    print(prcnt)
    say(prcnt[0])


if __name__ == "__main__":
    greet()
    while True:
        qry = tc().lower()

        if "time" in qry:
            time()

        elif "date" in qry:
            date()

        elif "wikipedia" in qry:
            say("What should I Search?")
            search = tc().lower()
            qry = qry.replace("wikipedia", search)
            result = wikipedia.summary(qry, sentences=2)
            say(result)

        elif "email" in qry:
            try:
                say("What would be the content of the Email?")
                contnt = tc()
                say("Recipient mail address would be?")
                recipient = input("Insert: ")
                mail(recipient, contnt)
                say("Mail sent Successfully!")
            except Exception as E1:
                say("Unable to send the Email because of:")
                say(E1)
                print(E1)

        elif "play" in qry:
            say("What would you like to play?")
            sng = tc()
            pywhatkit.playonyt(sng)
            engine.runAndWait()

        elif "chrome" in qry:
            say("What Should I search?")
            path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = tc().lower()
            wb.get(path).open_new_tab(search + ".com")
            engine.runAndWait()

        elif "remember" in qry:
            say("What should i remember?")
            data = tc()
            rm = open("data.txt", "w")
            rm.write(data)
            rm.close()

        elif "location" in qry:
            say("Which place you intend to Locate?")
            loc = tc()
            url = "https://www.google.com/maps/place/"+ loc + "/&amp;"
            say("Here is the Location of" +loc)
            webbrowser.get().open_new_tab(url)
            engine.runAndWait()

        elif "know anything" in qry:
            say("Lemme Check!")
            msg = open("data.txt", "r")
            say("You said to remember that")
            say(msg.read())
            print(msg.read())
            msg.close()

        elif "screenshot" in qry:
            ss()
            say("Screenshot saved at the location")

        elif "usage" in qry:
            say("CPU usage is at:")
            cpu()

        elif "battery" in qry:
            say("Battery is at:")
            btry()
            say("Percent")

        elif "joke" in qry:
            jokes()
            engine.runAndWait()
            """if "laughter" or "laugh" or "chuck" or "funny" in qry:
                jokes("chuck", "en")
            elif "neutral" in qry:
                jokes("neutral", "en")
            elif "twister" in qry:
                jokes("twister", "en")
            else:
                jokes("all", "en")"""

        elif "offline" in qry:
            engine.setProperty('rate', 250)
            hr = datetime.datetime.now().hour
            if 4 < hr < 20:
                say("Have a Nice Day ahead, Sir!")
            else:
                say("Good Night Sir.")
            quit()
