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
                print(f"User: {text}")
                speak("Sorry, I'm having trouble with my speech recognition.")
                exit()
            except Exception as e:
                while True:
                    speak("Sorry, I didn't catch that. Can you repeat?")
                    print(f"User: {text}")
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
    elif "how are you" or "how r u" in text:
        speak("I'm doing well. Thank you for asking.")
    elif "what is your name" in text:
        speak("My name is Jarvis.")
    elif "what can you do" in text:
            speak("I can search the internet for you. I can also tell you the time and the weather.")
    elif "who made you" or "who made u" in text:
        speak("I was made by a person named Soulucid. His information is available at https://guns.lol/soulucid/")
    elif "what is the time" in text:
        speak(time.ctime())
    elif "what is the weather" in text:
        speak("I'll search it up on the internet for you.")
        url = f"https://search.brave.com/search?q={text}"
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
