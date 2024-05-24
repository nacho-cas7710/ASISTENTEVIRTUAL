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
    rec = None 
    try:
        with sr.Microphone()as source:
            print("escuchando....")
            voice = listener.listen(source)
            rec= listener.recognize_google(voice,language='es-US')
            rec=rec.lower()
    except Exception as e:
        print(f"Error en listen: {e}")
                
    
    return rec
def reproduccion():
    talk("Que quieres reproducir")
    rec =listen()
    if rec is not None and 'reproduce' in rec:
        music = rec.replace('reproduce','')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    else:
        talk("No entendí la instrucción.")

reproduccion()