import ctypes
import json
import sys
import time
from urllib.request import urlopen
import os
import pyjokes
import pyttsx3
import speech_recognition as sr
import webbrowser

import google.generativeai as genai

import wikipedia
import winshell

from config import apikey
from config import apikey1
import datetime
import subprocess

text_speech = pyttsx3.init('sapi5')
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[0].id)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say("Good Morning !")

    elif 12 <= hour < 18:
        say("Good Afternoon !")

    else:
        say("Good Evening !")

    say("I am your Assistant")


def ai(prompt):
    genai.configure(api_key=apikey)

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    response = model.generate_content(prompt)
    response = response.text.replace("*", "")
    print(response)
    text = f"Gemini response for Prompt: {prompt} \n *************************\n\n"
    try:
        text += response
    except (KeyError, IndexError):
        # Handle exceptions where "text" key might not exist
        pass

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('ai')[1:]).strip()}.txt", "w") as f:
        f.write(text)

    return response


def say(text):
    print(text)
    text_speech.say(text)
    text_speech.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language="en-in")
        print(f"User said: {command}\n")

    except Exception as ec:
        print(ec)
        say("Unable to recognize your voice. My apologies.")
        return ""
    return command


def get_chat(prompt):
    genai.configure(api_key=apikey)

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    response = convo.last.text
    response = response.replace("*", "")
    convo.send_message(f"summarize {response} in 30 words or less")
    response = convo.last.text
    response = response.replace("*", "")
    say(response)


if __name__ == '__main__':
    say("Hello, I am Gemini")
    wishme()

    while True:
        query = take_command().lower()
        sites = ["youtube", "https://www.youtube.com"]

        if f"Open {sites[0]}".lower() in query:
            say(f"Opening {sites[0]} for you")
            webbrowser.open(sites[1])

        # if "open music" in query:
        # musicPath = "path to music"
        # subprocess.Popen([musicPath])

        elif "wikipedia" in query:
            try:
                say("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                say("According to wikipedia")
                say(results)
            except:
                say("Sorry, I could not find any results")


        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strfTime}")

        elif "open Chrome".lower() in query:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([chrome_path])


        elif 'search' in query or 'play' in query:
            query = query.replace("search", "?")
            query = query.replace("play", "?")
            webbrowser.open(query)

        elif 'joke' in query:
            say(pyjokes.get_joke())

        elif "Using AI".lower() in query:
            ai(prompt=query)

        elif 'news' in query:
            try:
                jsonObj = urlopen(
                    f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apikey1}")
                data = json.load(jsonObj)
                i = 1

                say('here are some top news')

                for item in data['articles']:
                    say(str(i) + '. ' + item['description'])
                    say(item['content'])
                    i += 1
                    say("Do you want me to continue?")
                    wish = take_command()
                    if "no" in wish:
                        say("Thank you for listening")
                        break

            except Exception as e:
                print(str(e))


        elif 'lock window' in query:
            say("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            say("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                say("Recycle Bin Recycled")
            except:
                say("Recycle Bin already empty")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            say("User asked to Locate")
            say(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            say("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            say("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])


        elif "write a note" in query:
            say("What should i write")
            note = take_command()
            if not os.path.exists("Note"):
                os.mkdir("Note")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            with open(f"Note/Note.txt", "w") as file:
                file.write(strTime)
                file.write(" :- ")
                file.write(note)

        elif "show me the note" in query:
            say("Showing Notes")
            file = open("Note/Note.txt", "r")
            say(file.read())

        elif "Bye".lower() in query:
            say("Goodbye!")
            sys.exit()

        else:
            try:
                get_chat(query)
            except:
                say("you should say something")
                take_command()
                continue
