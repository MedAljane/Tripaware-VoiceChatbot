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

    if x.lower() in ["english", "anglais"]:
        english(speaker, qu)

    elif x.lower() in ["french", "francais", "français"]:
        french(speaker, qu)