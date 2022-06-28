from chatOptions import loc, tim, desc, cor, mus, tripaware, langChange
from sentence_splitter import SentenceSplitter
from Tripaware.tripaware import getTripAware
from deep_translator import GoogleTranslator
from temperature import tempEN
from voiceSetup import Speaker
from bs4 import BeautifulSoup
from corona import getCorona
from queue import Queue
from time import sleep
import webbrowser
import pywhatkit
import requests
import datetime
import re

def hello_en(speaker, qu):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speaker.talk(qu, "Good morning!")
    elif hour>= 12 and hour<18:
        speaker.talk(qu, "Good afternoon!") 
    else:
        speaker.talk(qu, "Good evening!")


def english(speaker, qu):
    #anglais

    def city(speaker, qu):
        
        #city ​​description
        speaker.talk(qu, "choose the city please")
        ville=speaker.take_command(qu)

        try:
            l='https://fr.wikivoyage.org/wiki/'+ville
            p=requests.get(l)
            soup=BeautifulSoup(p.content , 'html.parser')
            pres=[]
            for i in soup.findAll('div',{'class':'mw-parser-output'}):
                for j in i.findAll('p'):
                    pres.append(j.text)
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
        

    
    speaker.setLanguage("en")
    hello_en(speaker, qu)

    speaker.talk(qu, "My name is Chatty, a chatbot created by Hassen Chebil and Mohamed Amine Aljane")
    speaker.talk(qu, "I can tell you about:")
    speaker.talk(qu, "Time, Weather, Corona, City Description, City Location, Music Listening, finding best trajectory (Tripaware)")
    speaker.talk(qu, "what do you want?")
    while True:
        command = speaker.take_command(qu)

        if command.lower() in tim:
            time(speaker, qu)
        
        elif command.lower() in desc:
            city(speaker, qu)

        elif command.lower() in cor:
            try:
                dates, cases, deaths = getCorona(speaker, qu)
            except:
                speaker.talk(qu, "Country not in our database!")
                continue

            speaker.talk(qu, "Here's the cases for the past 3 days:")
            for date, case, death in zip(dates, cases, deaths):
                speaker.talk(qu, date+": \n"+case+", "+death)

        elif command.lower() in mus:
            speaker.talk(qu, 'Choose the music please')
            song = speaker.take_command(qu)
            speaker.talk(qu, 'Playing ' + song + ', check your browser!')
            pywhatkit.playonyt(song)
            sleep(2)

        elif command.lower() in loc:
            speaker.talk(qu, 'Choose the city please!')
            l=speaker.take_command(qu)
            url = 'https://google.nl/maps/place/' + l + '/&amp;'
            webbrowser.open(url)
            speaker.talk(qu, "Opened location of "+l+" in google maps, check your browser.")
            sleep(2)

        elif  'weather' in command.lower():
            tempEN(speaker, qu)

        elif command in tripaware:
            getTripAware(speaker, qu)

        elif command.lower() in ["exit", "quitter", "quit", "cancel", "no"]:
            speaker.talk(qu, "Thank you for using our service, see you soon!")
            speaker.talk(qu, "exit")
            break
            
        elif command.lower() in langChange:
            from frenchVersion import french
            french(speaker, qu)

        speaker.talk(qu, 'Want something else?')
