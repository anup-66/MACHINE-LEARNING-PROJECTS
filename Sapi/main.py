import sys

import pyttsx3
from datetime import datetime
import speech_recognition as sr
from decouple import config as con
from random import choice
import utils
from utils import start_conv, greet_n, greet_m
import requests
from methods_use.off_methodes import open_camera, open_note, open_cmd, open_calc
from methods_use.onl_methods import get_random_joke, getadvice, weather_report, send_mail, \
    send_whatsapp_message, Google_search, play_on_youtube, search_on_wikipedia, find_my_ip

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


username = con('USERNAME')
name = con('NAME')
# name = "em chetenaaru"

def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {username} ")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon{username}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {username}")
    elif (hour >= 19) and (hour < 24):
        speak(f"i think you will work over night")
    elif (hour >= 24) and (hour < 6):
        speak(f"  It's late night You should sleep now")
    speak(f"I am {name}. How may I assist you?")


def user_say():
    rec = sr.Recognizer()
    data = sr.Microphone()
    with data as source:
        rec.adjust_for_ambient_noise(source, duration=1)
        print("Listening....")
        rec.pause_threshold = 0.5
        audio_voice = rec.listen(source)
    try:
        print("Analysing....")
        Speech = rec.recognize_google(audio_voice, language="en-in").lower()

        if not Speech in utils.Last_words:
            speak(choice(start_conv))

        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 24:
                speak("Good night sir, take care!")
            elif hour >= 2 and hour < 5:
                speak(choice(greet_n))
            elif 3 >= hour < 7:
                speak(choice(greet_m))
            else:
                speak('Have a good day sir!')
                speak(choice(utils.Normal_greet))
            exit("pls Start over to interact with me again. ")
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        Speech = 'None'
        # print(speech)
    return Speech

def Youtube():
    speak('What do you want to play on Youtube, sir?')
    speak("if possible please say the keywords it makes my work easier")
    video = user_say().lower()
    return video


if __name__ == '__main__':
    print(f"pls say help to know what {name} can do")
    print(f"pls say hello {name} to interact with me")
    greet_user()

    while True:

        speech = user_say().lower()
        print(speech)

        if 'open notepad' in speech:
            open_note()

        elif 'command prompt' in speech:
            open_cmd()

        elif 'open camera' in speech:
            open_camera()

        elif 'help' in speech or 'help me ' in speech or 'how can u help me' in speech:
            speak("I can help you in many ways. For your convenience I am printing it, Please have a look at it")
            print(utils.help)

        elif 'ip address' in speech:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n To make it easy , I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in speech:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = user_say().lower()
            print(search_query)
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("see its here on the terminal window, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in speech:
            Video = Youtube()
            speak("Is this what you told. Please confirm by saying yes")
            Conr = user_say().lower()
            if(Conr=="yes"):
                print("pls Start over to interact with me again.I am leaving watch your favorite video bye take care ")
                play_on_youtube(Video)
            # exit("pls Start over to interact with me again.I am leaving watch your favorite video bye take care ")
                exit()
            # else:
            #     speech ="youtube"

        elif 'google' in speech:
            speak('What do you want to search on Google, sir?')
            speech = user_say().lower()
            if not "none" in speech:
                Google_search(speech)

        elif "whatsapp" in speech:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = user_say().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "email" in speech:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = user_say().capitalize()
            speak("What is the message sir?")
            message = user_say().capitalize()
            if send_mail(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in speech:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif "advice" in speech:
            speak(f"Here's an advice for you, sir")
            advice = getadvice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)

        elif 'open calculator' in speech:
            open_calc()


        #elif "hello" in speech or "hi sapi " in speech or "hey " in speech or "hey sapi in speech ":
             #   speak(choice(utils.hello))

        elif 'weather' in speech:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif speech in utils.name:
            speak("ya sure tell me ur name ")
            Name = user_say().lower()
            utils.rem_name(Name)
            speak(f"i know ur name now its {utils.a[1]}")
        else:
            if ('none' not in speech):
                results = search_on_wikipedia(speech)
                #results = Google_search(speech)
                speak(results)
                speak("For your convenience, I am printing it on the screen sir.")
                print(results)


