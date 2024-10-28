import pyttsx3
s= input("enter anything to speak:")
engine = pyttsx3.init()
engine.say(s)
engine.runAndWait()