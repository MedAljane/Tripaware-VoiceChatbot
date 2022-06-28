from chatOptions import loc, tim, desc, cor, mus, tripaware, langChange
from Tripaware.tripaware import getTripAware
from temperature import tempFR
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

def hello_fr(speaker, qu):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speaker.talk(qu, "Bonjour !")
    elif hour>= 12 and hour<18:
        speaker.talk(qu, "Bonne après-midi !") 
    else:
        speaker.talk(qu, "Bonsoir !")


def french(speaker, qu):
    #francais

    def descriptionLieu(speaker, qu):
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
            speaker.talk(qu, pres_ville)
        except:
            speaker.talk(qu, 'Nom de ville incorrect ou introuvable...')


    def time(speaker, qu):
        time = datetime.datetime.now().strftime('%I:%M %p')
        speaker.talk(qu, "L'heure actuelle est " + time)
        
    
    speaker.setLanguage("fr")
    hello_fr(speaker, qu)
    
    speaker.talk(qu, "Je m'appelle Chatty, un chatbot créé par Hassen Chebil et Mohamed Amine Aljane.")       
    speaker.talk(qu, "Je peux vous parler de:")
    speaker.talk(qu, "Heure, Météo, Corona, Description d'un lieu, Localisation d'un lieu, Ecouter une musique, trouver la meilleure trajectoire (Tripaware)")
    speaker.talk(qu, "Que voulez-vous?")
    while True:
        command = speaker.take_command(qu)
        
        if command in desc:
            descriptionLieu(speaker, qu)
    
        elif command in tim:
            time(speaker, qu)

        elif 'météo' in command :
            tempFR(speaker, qu)

        elif command in mus: 
            speaker.talk(qu, "Choisissez la musique s'il vous plait")
            song = speaker.take_command(qu)
            speaker.talk(qu, 'playing ' + song + ', vérifiez votre navigateur!')
            pywhatkit.playonyt(song)
            sleep(2)

        elif  command in cor:
            try:
                dates, cases, deaths = getCorona(speaker, qu)
            except:
                speaker.talk(qu, "Pays n'est pas dans notre base de données !")
                continue
            
            speaker.talk(qu, "Voici les cas des 3 derniers jours:")
            for date, case, death in zip(dates, cases, deaths):
                speaker.talk(qu, date+": \n"+case+", "+death)

        elif command in loc:
            speaker.talk(qu, "Choisissez le lieu s'il vous plait")
            l = speaker.take_command(qu)
            url = 'https://google.en/maps/place/' + l + '/&amp;'
            webbrowser.open(url)
            speaker.talk(qu, "L'emplacement de " + l + ' ouvert dans google maps, vérifiez votre navigateur!')
            sleep(2)

        elif command in tripaware:
            getTripAware(speaker, qu)

        elif command.lower() in ["exit", "quitter", "quit", "cancel", "non"]:
            speaker.talk(qu, "Merci d'utiliser notre service, à bientôt!")
            speaker.talk(qu, "exit")
            exit()

        elif command.lower() in langChange:
            from englishVersion import english
            english(speaker, qu)

        speaker.talk(qu, 'Vous voulez autre chose?')
