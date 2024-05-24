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

translator=Translator()

texto=''
resultado=''
contador= 0
contador2 =0
saber =0


def talk(text):
    engine.say(text)
    engine.runAndWait()
def talk2(text):
    engine2= pyttsx3.init()
    voices= engine2.getProperty('voices')
    engine2.setProperty("voice", voices[1].id)
    engine2.say(text)
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

def listen2():
    try:
        with sr.Microphone()as source:
            print("escuchando....")
            voice = listener.listen(source)
            rec= listener.recognize_google(voice)
            rec=rec.lower(0)
    except:
        pass
    return rec


def empezar():
    global texto
    global resultado
    global contador
    global contador2
    global saber
    print ("¿Quieres traducir de ingles al español o del español al ingles ")
    talk  ("¿Quieres traducir de ingles al español o del español al ingles ")
    rec = listen2()
    if "del ingles al español" in rec:
        print("¿Qué quieres decir?")
        talk("¿Qué quieres decir?")
        rec=listen2()
        if " " in rec:
            texto=rec
            resultado=str(translator.translate(texto, src ="en", dest= "es"))
            for i in resultado :
                contador += 1
                if i == ",":
                    contador2 += 1
                    if contador2 == 3:
                        saber=contador
                        contador2= 0
                        talk(resultado[33:saber])
                        print(resultado)
                    else:
                        pass
    else:
        print("¿Qué quieres decir?")
        talk("¿Qué quieres decir?")
        rec=listen()
        if " " in rec:
            texto=rec
        resultado=str(translator.translate(texto, src ="es", dest= "en"))
        for i in resultado :
            contador += 1
            if i == ",":
                contador2 += 1
                if contador2 == 3:
                    saber = contador
                    contador2= 0
                    talk2(resultado[33:saber])
                    print(resultado)
            else:
                pass


empezar()

