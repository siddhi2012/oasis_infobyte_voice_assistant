import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import pyjokes
import smtplib
import datetime
import requests
from bs4 import BeautifulSoup
import random
import re
import pywhatkit
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant. How can I assist you today?")

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing....")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query.lower()

def perform_google_search(query):
    try:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for {query}")
    except Exception as e:
        speak("Sorry, I encountered an error while performing the search.")

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=3)
        speak("Here is some information:")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There were multiple matches. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        speak("Sorry, I couldn't find any information on that topic.")

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def greet():
    speak("Hello! How can I assist you today?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Unable to Recognize the voice.")
        return "None"

def main():
    greet()
    while True:
        command = listen()
        if "friday" in command:
            greet()
        elif "how are you" in command:
            speak("I am fine, Thank you")
            speak(f"How are you, {os.getlogin()}?")
        elif "who am i" in command:
            speak(os.getlogin())
        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak(f"A very {command}")
            speak("Thank you for wishing me! Hope you are doing well!")
        elif 'fine' in command or "good" in command:
            speak("It's good to know that you're fine.")
        elif "who are you" in command:
            speak("I am your virtual assistant.")
        elif "change my name to" in command:
            speak("What would you like me to call you, Sir or Madam?")
            new_name = takeCommand()
            speak(f'Hello again, {new_name}')
        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam?")
            new_name = takeCommand()
            speak(f"Thank you for naming me, {new_name}!")
        elif "what's your name" in command:
            speak(f"People call me {new_name}")
        elif 'time' in command:
            get_time()
        elif 'wikipedia' in command:
            speak('Searching Wikipedia')
            command = command.replace("wikipedia", "")
            search_wikipedia(command)
        elif 'open youtube' in command:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'play song in youtube' in command:
            speak("Sure! Please specify the name of the song you want to play.")
            song_name = listen()
            if song_name != "None":
                speak(f"Playing {song_name} on YouTube.")
                pywhatkit.playonyt(song_name)
            else:
                speak("Sorry, I couldn't understand the song name. Please try again.")
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")
        elif 'play music' in command or "play song" in command:
            speak("Enjoy the music!")
            music_dir = "D:\BCA\Projects\Python_Projects\Codeclause\CodeClauseInternship_MusicPlayerInPython\Music"  # Replace with your music directory
            songs = os.listdir(music_dir)
            if songs:
                song = os.path.join(music_dir, random.choice(songs))
                os.system(f'start {song}')
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'exit' in command:
            speak("Goodbye!")
            exit()
        elif "will you be my gf" in command or "will you be my bf" in command:
            speak("I'm not sure about that. Maybe you should give me some time.")
        elif "i love you" in command:
            speak("Thank you! But, It's a pleasure to hear it from you.")
        elif 'search' in command:
            command = command.replace("search", "")
            perform_google_search(command)
        else:
            speak("Sorry, I can't assist with that request.")

if __name__ == '__main__':
    main()