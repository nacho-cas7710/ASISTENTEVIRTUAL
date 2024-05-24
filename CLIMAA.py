import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess as sub
from googletrans import Translator
import requests
import AVMSpeechMath as sm
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser as web
import pyautogui
from time import sleep

engine= pyttsx3.init()
listener=sr.Recognizer()
voices=engine.getProperty('voices')
VELOCIDAD=115
engine.setProperty('voices', VELOCIDAD )
def talk(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    try:
        with sr.Microphone()as source:
            print("escuchando....")
            voice = listener.listen(source)
            rec= listener.recognize_google(voice,language='es-US')
            rec=rec.lower()
                
    except:
        pass
    return rec

def run_mike():
    talk("En que ciudad quieres saber el clima?")
    rec = listen()
    if "" in rec:
        city = rec
        url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=80c9a9ed3e6bbe5706193b756f7e8e7c&units=metric".format(city)
        res= requests.get(url)
        data= res.json()
        temp= data["main"]["temp"]
        wind_spped = data["wind"]["speed"]
        latitude= data["coord"]["lat"]
        longitud= data["coord"]["lon"]
        description = data["weather"][0]["description"]
        talk("la temperatura es: "+ str(float(temp)))
        print("temperatura: ", temp)
        talk(" la velocidad del tiempo:  " + str(float(wind_spped)))
        print("velocidad del tiempo:  ", wind_spped, "m/s")
        talk("la latitud: "+ str(latitude))
        print("latitud: ",latitude)
        talk("la longitud: "+ str(longitud))
        print("longitud: ",longitud)
        talk(description)
        print("descripcion: ", description)

run_mike()