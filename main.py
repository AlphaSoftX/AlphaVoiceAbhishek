# imports
import warnings
import time
import random
from sys import exit
from functions import clear, wishMe, username, takeCommand, speakAndWrite, use, newCommandQuotes
from logic import runQuery
from colors import green, yellow

# disabling unnecessary warnings
warnings.filterwarnings("ignore")

# global variables
upc = None

# clearing window
clear()

# wishing the user
wishMe()
speakAndWrite(f"\nWelcome M{use[0]}. {username()}", green)
time.sleep(0.25)
speakAndWrite(f"How can I help you {use[2]}?\n", yellow)

# starting program
while True:
    query = takeCommand().lower()
    time.sleep(.25)
    if "exit" in query or "bye" in query:
        speakAndWrite(f"Thanks for giving me your precious time {use[2]}, have a nice day!", green)
        break
    elif "repeat" in query or (("upper" in query or "last" in query) and "command" in query):
        if upc == None:
            print('No last command found!')
        else:
            runQuery(upc)
    else:
        runQuery(query)
        upc = query
    print()
    speakAndWrite(random.choice(newCommandQuotes) + f" {use[2]}?", yellow)
    time.sleep(1)

# turning off program
time.sleep(.25)
exit()
