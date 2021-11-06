import pyttsx3 as p #pip install pytysx3

engine = p.init()


#For changing the voice of the Assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#For saving the audio as a mp3
engine.save_to_file('Sentence to say', 'Test.mp3')
engine.runAndWait()

#For changing volume of the sentence
v = engine.getProperty('volume')
print("Original Volume =", v)
engine.setProperty('volume', 1.0) #Range 0-1

#For changing playback rate of the sentence
r = engine.getProperty('rate')
print("Original: ", r)
engine.setProperty('rate', 450)


engine.say("Hello, THis is a Test Run.")
engine.runAndWait()
