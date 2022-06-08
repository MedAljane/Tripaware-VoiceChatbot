from chatOptions import loc, tim, book, cor, mus, tripaware
from Tripaware.tripaware import getTripAware
from deep_translator import GoogleTranslator
from temperature import tempEN, tempFR
import speech_recognition as sr
from voiceSetup import Speaker
from bs4 import BeautifulSoup
from corona import getCorona
from threading import Thread
from queue import Queue
import pandas as pd
import webbrowser
import wikipedia
import pywhatkit
import requests
import datetime
import pyttsx3
import pyjokes
import ipinfo
import json 
import os
import re


def french(speaker, qu):
    #francais

    def Ville(qu):
        #​​Description de la ville
        speaker.talk(qu, "choisissez la ville s'il vous plait")
        ville = speaker.take_command(qu)
        l='https://fr.wikivoyage.org/wiki/'+ville
        p=requests.get(l)
        soup=BeautifulSoup(p.content , 'html.parser')
        pres=[]
        for i in soup.findAll('div',{'class':'mw-parser-output'}):
            for j in i.findAll('p'):
                pres.append(j.text)
        try:
            pres_ville=pres[2]+pres[3]
            pres_ville = re.sub(r'\[[0-9]*\]', ' ', pres_ville)
            pres_ville = re.sub(r'\s+', ' ', pres_ville)
            talk(pres_ville)
        except:
            speaker.talk(qu, 'Nom de ville incorrect ou introuvable...')


    def hello_fr(qu):
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            speaker.talk(qu, "Bonjour !")
        elif hour>= 12 and hour<18:
            speaker.talk(qu, "Bonne après-midi !") 
        else:
            speaker.talk(qu, "Bonsoir !")  
        speaker.talk(qu, "comment puis-je vous aider !")


    def reserv(speaker, qu):
        speaker.talk(qu, "OK, choisissez la ville, s'il vous plaît ")
        dest_ville=speaker.take_command(qu)
        speaker.talk(qu, "OK")
        webbrowser.open('https://www.booking.com/city/tn/'+dest_ville)

    def time(speaker, qu):
        time = datetime.datetime.now().strftime('%I:%M %p')
        speaker.talk(qu, "L'heure actuelle est " + time)
        

    while True:
        command = speaker.take_command(qu)
        

        if command in book :
            reserv(speaker, qu)
    
        elif command in tim:
            time(speaker, qu)

        elif 'météo' in command :
            tempFR(speaker, qu)

        elif command in mus: 
            speaker.talk(qu, "Choisissez la musique s'il vous plait")
            song = speaker.take_command(qu)
            speaker.talk(qu, 'playing ' + song)
            pywhatkit.playonyt(song)

        elif  command in cor:
            try:
                dates, cases, deaths = getCorona(speaker, qu)
            except:
                if speaker.lang == "en":
                    speaker.talk(qu, "Country not in our database!")
                    return None
                elif speaker.lang =="fr":
                    speaker.talk(qu, "Pays n'est pas dans notre base de données !")
                continue
            
            speaker.talk(qu, "Voici les cas des 5 derniers jours:")
            for date, case, death in zip(dates, cases, deaths):
                speaker.talk(qu, date+": \n"+case+", "+death)

        elif "qu'est-ce que" in command:
            thing = command.replace("qu'est-ce que", '')
            wikipedia.set_lang("fr")
            info_th = wikipedia.summary(thing, 2)
            talk(info_th)

        elif command in loc:
            speaker.talk(qu, "choisissez le lieu s'il vous plait")
            l = speaker.take_command(qu)
            url = 'https://google.nl/maps/place/' + l + '/&amp;'
            webbrowser.open(url)

        elif command in tripaware:
            getTripAware(speaker, qu)

        elif command.lower() in ["exit", "quitter", "quit", "cancel"]:
            speaker.talk(qu, "Merci d'utiliser notre service, à bientôt!")
            speaker.talk(qu, "exit")
            exit()

        speaker.talk(qu, 'Vous voulez autre chose?')
