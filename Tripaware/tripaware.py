from datetime import datetime  # For time manipulation
from Tripaware.sevDetails import getsSeveralDetails
import requests  # For executing requests
from Tripaware.Results import Results
from voiceSetup import Speaker

# Services importing

def getTripAware(transport, speaker, criteria=""):
    vtc = ["vtc", "taxi", "vtc and taxi"]
    bus = ["bus", "navette", "bus et navette"]
    covoiturage = ["covoiturage", "co-voiturage", "voiturage", "carpooling"]
    intermodal = ["intermodal", "intermodale", "train"]

    if transport.lower() in vtc:
        from Tripaware.Services.useVtcTaxi import getVtcTaxi
        if speaker.lang == 'en':
            speaker.talk("Welcome to VTC and Taxi reservation!")
        elif speaker.lang == 'fr':
            speaker.talk("Bienvenue sur réservation VTC et Taxi!")
        depDetails, arrDetails, date, time, passengers = getsSeveralDetails(speaker)

        if speaker.lang == 'en':
            speaker.talk("Searching for offers, please wait...")
        elif speaker.lang == 'fr':
            speaker.talk("En cours de la recherche d'offres, veuillez attendre...")

        fileName = getVtcTaxi(depDetails, arrDetails, date, time, passengers, speaker)

        if fileName == False:
            if speaker.lang == 'en':
                speaker.talk("Can't find offers for the desired inputs!")
            elif speaker.lang == 'fr':
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités !")
        else:
            result = Results(fileName)
            if criteria != "":
                result.showResults(fileName, speaker, criteria)
            else:
                result.showResults(fileName, speaker)
    
    elif transport.lower() in bus:
        from Tripaware.Services.useShuttleBus import getShuttleBus
        if speaker.lang == 'en':
            speaker.talk("Welcome to navette and bus reservation!")
        elif speaker.lang == 'fr':
            speaker.talk("Bienvenue sur réservation navette et bus!")

        depDetails, arrDetails, date, time, passengers = getsSeveralDetails(speaker)

        if speaker.lang == 'en':
            speaker.talk("Searching for offers, please wait...")
        elif speaker.lang == 'fr':
            speaker.talk("En cours de la recherche d'offres, veuillez attendre...")
        fileName = getShuttleBus(depDetails, arrDetails, date, time, passengers, speaker)

        if fileName == False:
            if speaker.lang == 'en':
                speaker.talk("Can't find offers for the desired inputs!")
            elif speaker.lang == 'fr':
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités !")
        else:
            result = Results(fileName)
            if criteria != "":
                result.showResults(fileName, speaker, criteria)
            else:
                result.showResults(fileName, speaker)
        
    elif transport.lower() in covoiturage:
        from Tripaware.Services.useCarpooling import getCarpooling
        if speaker.lang == 'en':
            speaker.talk("Welcome to carpooling reservation!")
        elif speaker.lang == 'fr':
            speaker.talk("Bienvenue à la réservation de covoiturage!")

        depDetails, arrDetails, date, time, passengers = getsSeveralDetails(speaker)

        if speaker.lang == 'en':
            speaker.talk("Searching for offers, please wait...")
        elif speaker.lang == 'fr':
            speaker.talk("En cours de la recherche d'offres, veuillez attendre...")
        fileName = getCarpooling(depDetails, arrDetails, date, time, passengers, speaker)

        if fileName == False:
            if speaker.lang == 'en':
                speaker.talk("Can't find offers for the desired inputs!")
            elif speaker.lang == 'fr':
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités !")
        else:
            result = Results(fileName)
            if criteria != "":
                result.showResults(fileName, speaker, criteria)
            else:
                result.showResults(fileName, speaker)

    elif transport.lower() in intermodal:
        from Tripaware.Services.useIntermodal import getIntermodal
        if speaker.lang == 'en':
            speaker.talk("Welcome to the intermodal reservation!")
        elif speaker.lang == 'fr':
            speaker.talk("Bienvenue à la réservation intermodale!")
            
        depDetails, arrDetails, date, time, passengers = getsSeveralDetails(speaker)

        if speaker.lang == 'en':
            speaker.talk("Searching for offers, please wait...")
        elif speaker.lang == 'fr':
            speaker.talk("En cours de la recherche d'offres, veuillez attendre...")
        fileName = getIntermodal(depDetails, arrDetails, date, time, passengers, speaker)

        if fileName == False:
            if speaker.lang == 'en':
                speaker.talk("Can't find offers for the desired inputs!")
            elif speaker.lang == 'fr':
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités !")
        else:
            result = Results(fileName)
            if criteria != "":
                result.showResults(fileName, speaker, criteria)
            else:
                result.showResults(fileName, speaker)
    
    else:
        if speaker.lang == 'en':
            speaker.talk("Sorry but we can't find the desired transport method provided!")
        elif speaker.lang == 'fr':
            speaker.talk("Désolé mais nous ne trouvons pas le moyen de transport souhaité fourni!")
