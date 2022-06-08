from sentence_splitter import SentenceSplitter
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


def english(speaker, qu):
    #anglais

    def city(speaker, qu):
        
        #city ​​description
        speaker.talk(qu, "choose the city please")
        speaker.lang = "fr"
        ville=speaker.take_command(qu)
        l='https://fr.wikivoyage.org/wiki/'+ville
        speaker.lang = "en"
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
            splitter = SentenceSplitter(language='fr')
            sentence_list = splitter.split(pres_ville)
            translated_sentences = [GoogleTranslator(target='en').translate(element) for element in sentence_list]
            ville_pres=""
            for i in translated_sentences:
                ville_pres+=i
            speaker.talk(qu, ville_pres)
        except:
            speaker.talk(qu, 'City name incorrect or not found...Please try again')


    def time(speaker,qu):
        time = datetime.datetime.now().strftime('%I:%M %p')
        speaker.talk(qu, 'Current time is ' + time)
        

    while True:
        command = speaker.take_command(qu)

        if command.lower() in tim:
            time(speaker, qu)
        
        elif command.lower() in cor:
            try:
                dates, cases, deaths = getCorona(speaker, qu)
            except:
                continue

            speaker.talk(qu, "Here's the cases for the past 5 days:")
            for date, case, death in zip(dates, cases, deaths):
                speaker.talk(qu, date+": \n"+case+", "+death)

        elif "what is" in command.lower():
            thing = command.replace("what is", '')
            wikipedia.set_lang("fr")
            info_th = wikipedia.summary(thing, 2)
            speaker.talk(qu, info_th)

        elif 'thank' in command.lower():
            speaker.talk(qu, 'Bla mziya, you are welcome')
        
        elif command.lower() in mus:
            speaker.talk(qu, 'Choose the music please')
            song = speaker.take_command(qu)
            speaker.talk(qu, 'playing ' + song)
            pywhatkit.playonyt(song) 

        elif command.lower() in loc:
            speaker.talk(qu, 'Choose the city please')
            l=input("City name : ")
            url = 'https://google.nl/maps/place/' + l + '/&amp;'
            webbrowser.open(url)
        
        elif  'weather' in command.lower():
            tempEN(speaker, qu)

        elif command in tripaware:
            getTripAware(speaker, qu)

        elif command.lower() in ["exit", "quitter", "quit", "cancel"]:
            speaker.talk(qu, "Thank you for using our service, see you soon!")
            speaker.talk(qu, "Exit")
            break

        speaker.talk(qu, 'Want something else?')
