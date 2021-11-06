import datetime
import smtplib
import wikipedia
import speech_recognition as sr
import pyttsx3 as p
import webbrowser as wb

engine = p.init()


def say(audio):
    engine.say(audio)
    engine.runAndWait()


# Speaking time
def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    say("Current Time is:")
    say(t)  # print(t)


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
    say("How may I help you today?")


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
        elif "chrome" in qry:
            say("What Should I search?")
            path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = tc().lower()
            wb.get(path).open_new_tab(search + ".com")
        elif "offline" in qry:
            quit()
