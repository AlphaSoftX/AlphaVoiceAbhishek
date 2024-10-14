# imports
import datetime
import time
import os
import pyttsx3
import speech_recognition as sr
from color import write, read
from colors import red, green, blue, yellow, cyan

# global variables
name = ""
gender = "m"
obj = {
    "m": ["r", "Sir", "sir"],
    "f": ["rs", "Mam", "mam"]
}
use = obj[gender]
engine = pyttsx3.init('sapi5')
newCommandQuotes = [f"Any command", f"Anything else", "Now, what could I do for you", "Would you like to ask for any other help", "Now, what would you like"]

# setting voice of program
if gender == "m":
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
else:
    engine.setProperty('voice', engine.getProperty('voices')[0].id)

# functions for the program
def takeInput():
    try:
        return read("> ", color=cyan)
    except:
        speakAndWrite(f"Sorry {use[2]}, could you write that again!", red)
        return takeInput()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        write("Listening...", color=cyan)
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        write("Recognizing...", color=cyan)
        query = r.recognize_google(audio, language='en-in')
        return query
    except:
        speakAndWrite(f"Sorry {use[2]}, could you repeat that!", red)
        return takeCommand()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def speakAndWrite(text, color):
    write(text, color=color)
    speak(text)


def username():
    global name
    speakAndWrite(f"What should I call you {use[2]}?", yellow)
    name = takeCommand()
    return name


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speakAndWrite(f"Good Morning {use[1]}!", green)
    elif hour >= 12 and hour < 16:
        speakAndWrite(f"Good Afternoon {use[1]}!", green)
    else:
        speakAndWrite(f"Good Evening {use[1]}!", green)
    time.sleep(0.25)
    speakAndWrite("I am your Assistant.", blue)
    write("AlphaVoice 2.0\n", color=blue)
    speak("AlphaVoice 2 point O")
    time.sleep(0.25)


def clear(): return os.system("cls")


def webbrowser(url):
    os.system("start chrome "+url)
