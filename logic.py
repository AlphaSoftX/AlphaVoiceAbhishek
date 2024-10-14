# imports
import pyjokes
import wikipedia
import datetime
import time
import subprocess
from functions import takeCommand, takeInput, username, webbrowser, speakAndWrite, speak, name, use
from color import write
from colors import green, red, blue, yellow, cyan, pink
from ecapture import ecapture as ec

# main logic function
def runQuery(query):
    global name
    if "hello" in query or query == "hi" or query.startswith("hi "):
        speakAndWrite(f"Hello {use[2]}!", green)
    elif "time" in query and "date" in query:
        dt = (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30))
        speakAndWrite(f"{use[1]}, the date is {dt.strftime('%B %d, %Y (%A)')} and the time is {dt.strftime('%H:%M:%S')}!", green)
    elif "date" in query:
        speakAndWrite(f"{use[1]}, the date is {(datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).strftime('%B %d, %Y (%A)')}!", green)
    elif "time" in query:
        speakAndWrite(f"{use[1]}, the time is {(datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).strftime('%H:%M:%S')}!", green)
    elif "joke" in query:
        speakAndWrite(f"{use[1]} your joke is:", blue)
        time.sleep(.25)
        speakAndWrite(pyjokes.get_joke(), green)
        time.sleep(0.5)
        speakAndWrite("Ha Ha Ha!", blue)
    elif ("created" in query or "made" in query) and "you" in query:
        speakAndWrite(f"{use[1]}, I was made by Mr. Arun!", green)
    elif "who are you" in query:
        speakAndWrite(f"{use[1]}, I am  your Assistant!", green)
        time.sleep(.25)
        write("AlphaVoice 2.0", color=blue)
        speak("AlphaVoice 2 point O")
    elif "what are you doing" in query:
        speakAndWrite(f"I am  just following your commands {use[2]}!", green)
    elif "favourite food" in query:
        speakAndWrite("I love to eat Pizza!", green)
    elif "old" in query:
        speakAndWrite("I am a few days old chatbot made by Mr. Arun!", green)
    elif "stop" in query:
        speakAndWrite("For how much time you want to stop me from taking commands?", yellow)
        try:
            ans = int(takeInput())
            write("AlphaVoice", color=blue, end=" ")
            write("turned off!", color=green)
            speak("AlphaVoice turned off!")
            time.sleep(ans)
            write("AlphaVoice", color=blue, end=" ")
            write("restarted!", color=green)
            speak("AlphaVoice restarted!")
        except:
            speakAndWrite("Some error occurred!", red)
    elif "who am i" in query or "who i am" in query:
        speakAndWrite(f"I think that you are a human and your name is M{use[0]}. {name}!", green)
    elif "reason for you" in query or "why you came to world" in query:
        speakAndWrite("I was created as a Minor project by Mr. Arun, but reason behind my creation is a secret!", green)
    elif "you mad" in query or "shut up" in query or "really" in query:
        speakAndWrite("Sorry, did I said something wrong!", red)
    elif "how are you" in query:
        write(f"I am fine {use[2]}!", color=green, end=" ")
        write("How are you?", color=yellow)
        speak(f"I am fine {use[2]}! How are you?")
        ans = takeCommand().lower()
        if "good" in ans or "fine" in ans or "happy" in ans:
            speakAndWrite(f"I am glad to see you fine {use[2]}!", green)
        else:
            speakAndWrite("I think you should talk to anyone else about this matter!", red)
    elif "love" in query:
        speakAndWrite("It is 7th sense that destroy all other senses!", pink)
    elif "change" in query and "name" in query:
        speakAndWrite(f"Now, your name is M{use[0]}. {username()}!", green)
    elif "my" in query and "name" in query:
        speakAndWrite(f"{use[1]}, your name is M{use[0]}. {name}!", green)
    elif "your" in query and "name" in query:
        write(f"{use[1]}, my name is", color=green, end=" ")
        write("AlphaVoice", color=blue, end="")
        write("!", color=green)
        speak(f"{use[1]}, my name is AlphaVoice!")
    elif "calculate" in query:
        speakAndWrite("Write your sum!", cyan)
        ans = takeInput().lower()
        time.sleep(.25)
        try:
            ans = eval(ans)
            write("Your answer is", color=green, end=" ")
            write(ans, color=blue)
            speak(f"Your answer is {ans}")
        except:
            speakAndWrite("Some error occurred!", red)
    elif "camera" in query or ("take" in query and ("photo" in query or "pic" in query)):
        ec.capture(0, "AlphaCam", "image.png")
    elif "open" in query and "youtube" in query:
        speakAndWrite("Opening YouTube...", green)
        webbrowser("youtube.com")
    elif "open" in query and "google" in query:
        speakAndWrite("Opening Google...", green)
        webbrowser("google.com")
    elif "hungry" in query:
        speakAndWrite(f"I think you should order something {use[2]}!", green)
        speakAndWrite("Opening Zomato...", green)
        webbrowser("zomato.com")
    elif "visit" in query or ("book" in query and "cab" in query):
        speakAndWrite("Opening OlaCabs...", color=green)
        webbrowser("olacabs.com")
    elif "open" in query and "website" in query:
        speakAndWrite(f"Which website should I open {use[2]}?", yellow)
        ans = takeInput().lower()
        speakAndWrite("Opening...", green)
        webbrowser(ans)
    elif "restart" in query:
        speakAndWrite("This will restart your computer!", green)
        time.sleep(.25)
        write("Are you sure? (Y/n)", color=cyan)
        speak("Are you sure?")
        ans = takeInput().lower()
        if ans == "" or ans == "y" or "yes" in ans:
            time.sleep(.25)
            speakAndWrite("Restarting...", green)
            subprocess.call("shutdown /r")
    elif "shut down" in query:
        speakAndWrite("This will shut down your computer!", green)
        time.sleep(.25)
        write("Are you sure? (Y/n)", color=cyan)
        speak("Are you sure?")
        ans = takeInput().lower()
        if ans == "" or ans == "y" or "yes" in ans:
            time.sleep(.25)
            speakAndWrite("Shutting down...", green)
            subprocess.call("shutdown /p /f")
    elif "locate" in query:
        speakAndWrite(f"What should I locate {use[2]}?", yellow)
        location = takeCommand()
        speakAndWrite(f"Locating {location}...", green)
        location = location.replace(" ","+")
        webbrowser("https://www.google.com/maps/search/"+location)
    elif "wikipedia" in query:
        speakAndWrite(f"What should I search {use[2]}?", yellow)
        ans = takeCommand().lower()
        speakAndWrite("Searching Wikipedia...", green)
        try:
            results = wikipedia.summary(ans, sentences=3)
            speakAndWrite("According to Wikipedia:", blue)
            time.sleep(.25)
            speakAndWrite(results, green)
        except:
            speakAndWrite("Some error occurred while searching!", red)
    elif "write" in query and "note" in query:
        speakAndWrite(f"What should i write, {use[2]}?", yellow)
        note = takeInput().replace("  ", "\n")
        file = open("note.txt", "w")
        speakAndWrite(f"{use[1]}, should I include date and time?", cyan)
        sidt = takeCommand()
        if "yes" in sidt:
            dt = (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).strftime("%B %d, %Y (%A) %H:%M:%S")
            file.write(dt)
            file.write("\n")
            file.write(note)
        else:
            file.write(note)
        file.close()
    elif "show" in query and "note" in query:
        speakAndWrite("Showing Note...", green)
        try:
            file = open("note.txt", "r")
            write(file.read(), color=blue)
            speak(f"Here is your note {use[2]}!")
            file.close()
        except:
            speakAndWrite("No note found, please use 'write note' command!", red)
    else:
        speakAndWrite(f"{use[1]}, I think you should talk to anyone else about this matter!", red)
        time.sleep(.25)
        write("Do you want me to search your query on google! (Y/n)", color=cyan)
        speak("Do you want me to search your query on google!")
        ans = takeInput().lower()
        if ans == "" or ans == "y" or "yes" in ans:
            time.sleep(.25)
            speakAndWrite("Searching...", green)
            webbrowser("google.com/search?q="+query.replace(" ","+"))
