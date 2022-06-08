from queue import Queue
from voiceSetup import Speaker
from frenchVersion import french
from englishVersion import english

def chatbot(qu):

    speaker = Speaker("fr")
    speaker.talk(qu, 'Voulez-vous parler en anglais ou en français?')
    while True:
        x = speaker.take_command(qu)

        if x.lower() in ["english", "anglais", "french", "francais", "français"]:
            break
            
        else :
            if speaker.lang == "fr":
                speaker.talk(qu, "langue non prise en charge, choisissez à nouveau s'il vous plaît!")
            elif speaker.lang == "en":
                speaker.talk(qu, "language not supported, choose again please!")

    if x in ["english", "anglais"]:
        speaker.setLanguage("en")
        
        speaker.talk(qu, "My name is Chatty, a chatbot created by Hassen Chebil and Mohamed Amine Aljane")
        speaker.talk(qu, "I can tell you about:")
        speaker.talk(qu, "Time, Weather, Corona, City Description, City Location, Music Listening, finding best trajectory (Tripaware)")
        speaker.talk(qu, "what do you want?")
        english(speaker, qu)

    elif x.lower() in ["french", "francais", "français"]:
        speaker.setLanguage("fr")
        speaker.talk(qu, "Je m'appelle Chatty, un chatbot créé par Hassen Chebil et Mohamed Amine Aljane.")       
        speaker.talk(qu, "Je peux vous parler de:")
        speaker.talk(qu, "Heure, Météo, Corona, Description d'un lieu, Localisation d'un lieu, Ecouter une musique, trouver la meilleure trajectoire (Tripaware)")
        speaker.talk(qu, "Que voulez-vous?")
        french(speaker, qu)