from __future__ import print_function
import pickle
import os.path
import urllib
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import subprocess
import wolframalpha
import re
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import requests
import datetime
import wikipedia
import webbrowser as web
import os
import winshell
import pyjokes
import feedparser
import datetime
from datetime import datetime as dt
import time
from datetime import date
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import subprocess
import selenium
from selenium import webdriver
import wave
import pyaudio
import pyttsx3
import random
import playsound
import certifi
import ssl
import bs4 as bs
import smtplib
import operator
from pywinauto.application import Application
from wit import Wit
import psutil
from win10toast import ToastNotifier # shows notification on desktop
import threading # allows speech and desktop at same time





API_ENDPOINT = 'https://api.wit.ai/speech'
ACCESS_TOKEN = '4XF5AMXFSZCR3AKIPHFC676OTBWDZMW4'
client = Wit(ACCESS_TOKEN)



clientwol = wolframalpha.Client("WV4YW6-2E95V4AK88")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def birthday():
    today = datetime.date.today
    my_birthday = datetime.date(today().year, 10, 21)
    mum_birthday = datetime.date(today().year,7,1)
    if my_birthday == today:
        speak("Happy birthday, have a good one")
    else:
        return 0


def holidays():
    today = datetime.date.today
    print(today)
    christmas = datetime.date(today().year, 12, 24)
    new_year = datetime.date(today().year, 1, 1)
    if christmas == today:
        speak("Merry Christmas")
    if new_year == today:
        speak("Happy new year, may it be a blessed one!")
    else:
        return 0


def thetime():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak(Time)


def thedate():
    date = datetime.datetime.now().strftime("%A %B %d %Y")
    speak(date)


def welcome():
    # speak("Welcome, PAVA is now online!")
    birthday()
    holidays()
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:

        speak("Good Morning, how may PAVA assist you!")
    elif hour >= 12 and hour < 18:

        speak("Good Afternoon, how may PAVA assist you! !")

    else:

        speak("Good Evening, how may PAVA assist you!  !")


welcome()






r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:

def get_audio():
        r = sr.Recognizer()
        speech = sr.Microphone()
        with speech as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            said = ""
        try:
            said = r.recognize_wit(audio, key="4XF5AMXFSZCR3AKIPHFC676OTBWDZMW4")
            print("You said: " + said)
        except sr.UnknownValueError:  
            speak('Sorry, I did not understand')
        except sr.RequestError:
            speak('Sorry, the service is down') 
        print(f">> {said.lower()}")  
        return said.lower()




def shutdown():
    if said == "shut down":
        speak("Shutting down system, goodbye!")
        os.system("shutdown /s /t 1")


def restart():
    if said == "restart":
        speak("restarting system, see you soon!")
        os.system("shutdown /r /t 1")

def note(text):
    date=datetime.datetime.now()
    file_name=str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])


def desktop():
    import pyautogui

    # go to desktop
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")


def terminology(terms):
    for term in terms:
        if term in said:
            return True


while True:
    print("Listening")
    said = get_audio()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    if percent < 20:
        if plugged == False:
            speak(" Hello, your battery is getting low, please charge it now")
            if plugged == True:
                speak("Thank you, I will inform you when next to unplug charging device")
    elif percent == 95:
        if plugged == True:
            speak(" Hello, charging is close to completion, please unplug charging device")
    if "current battery life" in said:
        speak(f"current battery life is {percent} %")



    if terminology(['hey','hi','hello']):
        greetings = ["hey, how can I help you", "hey, what's up? ",
                     "I'm listening ", "how can I help you?"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)
    if terminology(["what is your name","what's your name","tell me your name"]):
        speak("my name is PAVA, which stands for Python AI voice assistant")
    if terminology(["what can you do", "what do you do", "how can you help me", "how could you help", "how would you help"]):
        speak("currently, I can tell you the datetime, websearch and shutdown, or restart a system.")
    if terminology(["who is the best", "who's the best"]):
        speak("PAVA thinks you're the best")
    if terminology(["you're cool", "you are cool", "you are the best", "you're the best", "I think you are the best",
                "you are helpful", "you are very helpful", "you're helpful"]):
        speak("Thank you for saying so")
    if "shut down" in said:
        shutdown()
    if "restart" in said:
        restart()
    if "make a note" in said:
        said = get_audio()
        speak("noting  now")
        note_text = get_audio().lower()
        note(note_text)
        scribed = ["I copied this", "here is what you said ",
                    "I noted this "]
        written = scribed[random.randint(0, len(scribed) - 1)]
        speak(written)
        
    if "desktop" in said:
        desktop()

    if terminology(["search for", "search"]) and 'you tube' not in said:
        search_term = said.split("for")[-1]
        print(search_term)
        url = f"https://google.com/search?q={search_term}"
        web.get().open(url)
        speak(f'Here is what I found for {search_term} on google')
    if "thank you" in said:
        speak("you're welcome")
    if "you tube" in said:
        search_term = said.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        web.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
    if "wikipedia" in said:
        speak('Searching Wikipedia...')
        
        query = said.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

        


    if "dictate" in said:

        app = Application().start('notepad.exe')

        # Main window specification
        main_dlg = app.UntitledNotepad
        main_dlg.wait('visible')

        # Print all controls on the dialog
        main_dlg.print_control_identifiers()
        while True:
            said = get_audio()
            main_dlg.Edit.type_keys(said,
                                    with_spaces=True,
                                    with_newlines=True,
                                    pause=0,
                                    with_tabs=True)
            if "end" in said:
                speak("ending")
                break

    if terminology(["what is the time", "what time is it"]):
        speak(thetime())
    if terminology(["what is the date", "what is today's date", "what day is it", "what is the date today","what's the date"]):
        speak(thetime())
    if terminology(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        speak("It is "+cmove)
    if terminology(["okay stop now", "be quiet","nap","shut up"]):
        speak("okay, I will nap for a minute")
        time.sleep(60)




    if "goodbye" in said:
        speak("goodbye")
        exit()


