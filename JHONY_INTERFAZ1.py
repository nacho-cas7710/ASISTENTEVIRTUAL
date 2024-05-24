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
#from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser as web
import pyautogui
from time import sleep

from time import sleep
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from PIL import *
from itertools import count
import collections

def botones(rec):
    if rec == 1:
        from SPOTYFY import escuchar_cancion
        escuchar_cancion()
    if rec == 2:                                                                                                                
        
        from CLIMAA import run_mike
        run_mike()
    if rec == 3:
        from HORA import horita
        horita()
    if rec ==4:
        from MATEMATIC import matex
        matex()
    if rec ==5:
        from YOUTUBE import reproduccion
        reproduccion()
    if rec ==6:
        from WIKI import  wiki
        wiki()
    if rec ==7:
        from TRADUCTORRR import empezar
        empezar()
    if rec ==8:
        from CHISTE import chistazo
        chistazo()

        







class ImageLabel(tk.Label):
    
    def load(self, im):
        if isinstance (im, str):
            im =Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
         
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

print("holaa")
root = tk.Tk()
root.geometry("3000x3000")
root.config(background= "white", bg= "white")
lbl = ImageLabel(root, width=800, height=1100, background= "white")  #configuración tamaño del gif
lbl.pack()
lbl.load('robot.gif')   
miframe = Frame(root, width= 3000, height= 3000)
miframe.pack()

imagen5 = PhotoImage(file = "sp.png")
b = Button(root, text = "Click", image = imagen5, background= "white", bg = "white", command= lambda:botones(1)).place(x = 300, y = 20)

imagen6 = PhotoImage(file = "clima.png")
c = Button(root, text = "Click", image = imagen6, background= "white", bg = "white", command= lambda:botones(2)).place(x = 33, y = 200)

imagen9 = PhotoImage(file = "rolex.png")
c = Button(root, text = "Click", image = imagen9, background= "white", bg = "white", command= lambda:botones(3)).place(x = 1130, y = 460)

imagen10 = PhotoImage(file = "calculadoras.png")
c = Button(root, text = "Click", image = imagen10, background= "white", bg = "white", command= lambda:botones(4)).place(x = 33, y = 460)

imagen22 = PhotoImage(file = "insta2.png")
c = Button(root, text = "Click", image = imagen22, background= "white", bg = "white", command= lambda:botones(4)).place(x = 250, y = 460)

imagen24 = PhotoImage(file = "twitte30.png")
c = Button(root, text = "Click", image = imagen24, background= "white", bg = "white", command= lambda:botones(4)).place(x = 850, y = 460)

imagen25 = PhotoImage(file = "tiktikl.png")
c = Button(root, text = "Click", image = imagen25, background= "white", bg = "white", command= lambda:botones(4)).place(x = 480, y = 530)



imagen12 = PhotoImage(file = "yt.png")
c = Button(root, text = "Click", image = imagen12, background= "white", bg = "white", command= lambda:botones(5)).place(x = 55, y = 29)

imagen2 = PhotoImage(file = "wik.png")
c = Button(root, text = "Click", image = imagen2, background= "white", bg = "white", command= lambda:botones(6)).place(x = 1150, y = 250)

imagen44 = PhotoImage(file = "face.png")
c = Button(root, text = "Click", image = imagen44, background= "white", bg = "white", command= lambda:botones(6)).place(x = 950, y = 250)



imagen7 = PhotoImage(file = "tradu.png")
c = Button(root, text = "Click", image = imagen7, background= "white", bg = "white", command= lambda:botones(7)).place(x = 600, y = 3)

imagen33 = PhotoImage(file = "waths.png")
c = Button(root, text = "Click", image = imagen33, background= "white", bg = "white", command= lambda:botones(7)).place(x = 850, y = 0)





imagen1 = PhotoImage(file = "jk.png")
c = Button(root, text = "Click", image = imagen1, background= "white", bg = "white", command= lambda:botones(8)).place (x =1100 , y = 0)


                                                                                        





root.mainloop()