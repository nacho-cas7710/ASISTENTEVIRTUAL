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
#variables de spotify
client_id = "c56069979eca4ae88442bab9c5646f40"
client_secret = "f2a149e307194d749f25828b0c6e01c6"
author = ''
song = ''
flag = 0

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

def spoty():
    global flag
    global song
    if len(author) > 0:
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        result = sp.search(author)
        for i in range(0, len(result["tracks"]["items"])):
            name_song = result["tracks"]["items"][i]["name"]
            if song == name_song:
                web.open(result["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press("enter")
                break
    if flag == 0:
        song = song.replace(" ", "%20")
        web.open(f'spotify:search:{song}')
        sleep(5)
        for i in range(28):
            pyautogui.press("tab")
        pyautogui.press("enter")



def escuchar_cancion():
    global song
    talk("¿Qué canción quieres escuchar?")
    rec = listen()
    if "" in rec:
        song = rec.upper()
        spoty()
    else:
        pass
escuchar_cancion()


