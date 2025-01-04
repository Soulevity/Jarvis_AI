import speech_recognition as sr
import pyttsx3
import setuptools
import webbrowser
import requests
from bs4 import BeautifulSoup
import os
import time

recog = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! This is Jarvis.")   
    def listen():
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source)
            audio = recog.listen(source)
            try:
                return recog.recognize_google(audio)
            except sr.RequestError:
                print(f"User: {listen().lower()}")
                speak("Sorry, I'm having trouble with my speech recognition.")
                exit()
            except Exception as e:
                while True:
                    speak("Sorry, I didn't catch that. Can you repeat?")
                    print(f"User: {listen().lower()}")
                    with sr.Microphone() as source:
                          recog.adjust_for_ambient_noise(source)
                          audio = recog.listen(source)
                          try:
                                return recog.recognize_google(audio)
                          except sr.RequestError:
                            speak("Sorry, I'm having trouble with my speech recognition.")
                            exit()
                          except Exception as e:
                            continue

while True:
    speak("What can I do for you?")
    text = listen().lower()
    print(f"User: {text}")
    if "open" in text:
        speak("What do you want me to open?")
        open = listen().lower()
        if "youtube" in open:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")
        elif "google" in open:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com/")
        elif "brave" in open:
            speak("Opening Brave.")
            webbrowser.open("https://search.brave.com/")
        elif "discord" in open:
            speak("Opening Discord.")
            webbrowser.open("https://discord.com/")
        elif "github" in open:
            speak("Opening GitHub.")
            webbrowser.open("https://github.com/")
        elif "reddit" in open:
            speak("Opening Reddit.")
            webbrowser.open("https://www.reddit.com/")
        elif "twitter" in open:
            speak("Opening Twitter.")
            webbrowser.open("https://x.com/")
        elif "facebook" in open:
            speak("Opening Facebook.")
            webbrowser.open("https://www.facebook.com/")
        elif "instagram" in open:
            speak("Opening Instagram.")
            webbrowser.open("https://www.instagram.com/")
        elif "twitch" in open:
            speak("Opening Twitch.")
            webbrowser.open("https://www.twitch.tv/")
        elif "spotify" in open:
            speak("Opening Spotify.")
            webbrowser.open("https://open.spotify.com/")
        elif "amazon" in open:
            speak("Opening Amazon.")
            webbrowser.open("https://www.amazon.com/")
        elif "wikipedia" in open:
            speak("Opening Wikipedia.")
            webbrowser.open("https://www.wikipedia.org/")
        else:
            break
        break

    if "search" in text:
        speak("What do you want me to search for?")
        search = listen().lower()
        speak(f"Searching for {search}.")
        webbrowser.open(f"https://search.brave.com/search?q={search}")
    elif "exit" in text:
        speak("Goodbye!")
        break
    elif "stop" in text:
        break
    elif "hello" in text:
        speak("Hello! I think I am working properly.")
    elif "how are you" in text:
        speak("I'm doing well. Thank you for asking.")
    elif "what is your name" in text:
        speak("My name is Jarvis.")
    elif "what can you do" in text:
            speak("I can search the internet for you. I can also tell you the time and the weather.")
    elif "who made you" in text:
        speak("I was made by a person named Soulucid. His information is available at https://guns.lol/soulucid/")
    elif "what is the time" in text:
        speak(time.ctime())
    elif "what is the weather" in text:
        speak("I'll search it up on the internet for you.")
        url = f"https://search.brave.com/search?q=Weather near me"
        response = requests.get(url)
        open = webbrowser.open(url)
    elif "what is the news" in text:
        speak("I'll search it up on the internet for you.")
        url = f"https://search.brave.com/search?q=Latest news near me"
        response = requests.get(url)
        open = webbrowser.open(url)
    else:
        speak("I don't seem to have any relevant information about that. I'll search it up on the internet for you.")
        url = f"https://search.brave.com/search?q={text}"
        response = requests.get(url)
        open = webbrowser.open(url)
