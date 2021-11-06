import datetime
import pyttsx3 as p #pip install pytysx3

engine = p.init()


def say(audio):
    engine.say(audio)
    engine.runAndWait()


# Speaking time
def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    # "%H:%M:%S" WILL PRINT EXACT TIME, WHILE "%H:%R:%M" WILL GIVE TIME AND MONTH BOTH
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


date()
say("And")
time()
