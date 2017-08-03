from globals import *
import speech_recognition as sr
import datetime
import sys
from sys import platform
import os
import subprocess
from applemusic import AppleMusic
import randfacts
import pyautogui
import psutil
from PyDictionary import PyDictionary

def speak(audio):
    """
    Enables the virtual assistant to speak based on the required input.

    audio: text to be spoken

    """

    print("Karen: {}".format(audio))
    engine.say(audio)
    engine.runAndWait()

def GreetMe(name):
    """
    This function ensures that the virtual assistant greets the user by 
    their name.

    name: name of the user

    """

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning {}.".format(name))
        time = 'this morning'
    elif hour >= 12 and hour < 18:
        speak("Good afternoon {}.".format(name))
        time = 'today'
    else:
        speak("Good evening {}.".format(name))
        time = 'tonight'
    
    speak("You can call me Karen. What would you like me to do for you {}?".format(time))

def MyCommand():
    """
    Listens to the voice of the user to determine the command that the virtual 
    assistant must respond and the task it should accomplish.

    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        speak("Processing.")
        query = r.recognize_google(audio, language='en-us')
        print("User: {}\n".format(query))

    except sr.UnknownValueError:
        speak("Could you say that again?")
        return MyCommand()

    return query

def sendemail():
    """
    Virtual assistant sends an email to a specified recipent.

    """

    speak("Who should I send it to?")
    recipient = MyCommand().lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('email', 'password')
        speak("What would you like me to say?")
        content = MyCommand()
        server.sendmail('email', recipient, content)
        server.close()
        speak("Email sent.")
    except:
        speak("Sorry, {}. I couldn't send your email.".format(name))

def playsong():
    """
    Virtual assistant plays a specified song from apple music.

    """

    speak("What song would you like me to play?")
    song = MyCommand()

    try:
        AM = AppleMusic()
        AM.setupMethod()
        AM.setupVariables()
        AM.initiateWindow()
        AM.login('email', 'password')
        AM.playSong(song)
    except:
        speak("Sorry, {}. I couldn't play the song you requested.".format(name))

def screenshot():
    """
    Virtual assistant takes a screenshot and then saves it.

    """

    sc = pyautogui.screenshot()
    sc.save('my_screenshot.png')
    speak("Screenshot saved.")

def google(command):
    """
    Open a tab based on the specified google search term.

    command: command specified by the user

    """

    term = command.replace('google', '').strip()
    url = "https://www.google.com/search?q={}".format(term)
    return url

def youtube(command):
    """
    Open a tab based on the specified youtube search term.

    command: command specified by the user

    """

    term = command.replace('youtube', '').strip()
    url = "https://www.youtube.com/results?q={}".format(term)
    return url

def reminder():
    """
    Saves a reminder to a text file.

    """

    speak("What would you like me to remind you?")
    reminder = MyCommand()

    try:
        r = open('reminders.txt', 'w')
        r.write(reminder)
        r.close()
        speak("Reminder saved.")
    except:
        speak("Sorry, {}. I couldn't set a reminder.".format(name))

def secs2hours(secs):
    """
    Converts time in seconds to hours, minutes, and seconds

    secs: time in seconds

    """
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "{} hours, {} minutes, and {} seconds".format(hh, mm, ss)

def dictionary():
    """
    Gets the meaning of a word specific by the user.

    """

    speak("What word would you like to know the meaning of?")
    word = MyCommand().lower()

    try:
        dict = PyDictionary()
        meaning = dict.meaning(word) 
        speak(meaning)
    except:
        speak("I couldn't quite get that, could you repeat the word?")
        dictionary()

def findphone():
    """
    Find location of user's phone using iCloud

    """
    return 1

def weather():
    """
    Provides information about the weather in a specified city.

    """

    return 1

def news():
    """
    Provides the user with trending headlines.

    """
    return 1

def recaudio():
    """
    Records audio until user manually stops the recording.

    """

    return 1

def recvideo():
    """
    Records screen until user manually stops the recording.

    """

    return 1
    