from datetime import datetime  # For time manipulation
from Tripaware.sevDetails import getsSeveralDetails
import requests  # For executing requests
from Tripaware.Results import Results
from voiceSetup import Speaker

def checkProceeding(speaker):
    if speaker.lang == 'en':
        speaker.talk("would you like to proceed with the details of this choice or change the criteria?\na reminder about criteria offers: total C O 2 consumption, total price of the route, total distance or total duration.")
        speaker.talk("Change or proceed?")
        choice = speaker.take_command()

        if choice in ["change criteria", "change", "criteria"]:
            speaker.talk("Make a criteria choice please!")
            criteria = speaker.take_command()

            if criteria.lower() in ["total co2", "co2"]:
                return False, "TotalCo2"
            elif criteria.lower() in ["prix totale", "total price", "price", "prix"]:
                return False, "TotalPrice"
            elif criteria.lower() in ["duration totale", "total duration", "duration"]:
                return False, "TotalDuration"
            elif criteria.lower() in ["distance totale", "total distance", "distance"]:
                return False, "TotalDistance"
            else:
                return True, ""


        else:
            speaker.talk("Proceeding with details...")
            return True, ""

    elif speaker.lang == 'fr':
        speaker.talk("souhaitez-vous poursuivre le détail de ce choix ou modifier les critères ?\nRappel des critères : consommation totale de C O 2, prix total du parcours, distance totale ou durée totale.")
        speaker.talk("Changer ou poursuivre!")
        choice = speaker.take_command()
        
        if choice in ["changer critère", "changer", "critère"]:
            speaker.talk("Faites un choix de critères s'il vous plait!")
            criteria = speaker.take_command()

            if criteria.lower() in ["total co2", "co2", "total CO2"]:
                return False, "TotalCo2"
            elif criteria.lower() in ["prix totale", "total price", "price", "prix"]:
                return False, "TotalPrice"
            elif criteria.lower() in ["duration total", "durée totale", "total duration", "duration"]:
                return False, "TotalDuration"
            elif criteria.lower() in ["distance totale", "distance total", "total distance", "distance"]:
                return False, "TotalDistance"
            else:
                return True, ""
        else:
            speaker.talk("Proceeding with details...")
            return True, ""

def getTripAware(speaker, criteria=""):
    vtc = ["vtc", "taxi", "vtc and taxi"]
    bus = ["bus", "navette", "bus et navette"]
    covoiturage = ["covoiturage", "co-voiturage", "voiturage", "carpooling"]
    intermodal = ["intermodal", "intermodale", "train"]

    if speaker.lang == 'en':
        speaker.talk("Welcome to the tripaware service, where you can find the best mean of transport to go from point A to point B using different criterias.")
        speaker.talk("We offer you these means of transport, please choose one of them: vtc and taxi, navette and bus, carpooling, intermodal")
    elif speaker.lang == 'fr':
        speaker.talk("Bienvenue sur le service tripaware, où vous pouvez trouver le meilleur moyen de transport pour aller d'un point A à un point B selon différents critères.")
        speaker.talk("Nous vous proposons ces moyens de transport, merci d'en choisir un : vtc et taxi, navette et bus, covoiturage, intermodal")
        
    transport = speaker.take_command()

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
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités!")
        else:
            result = Results(fileName)

            proceed = False
            while not proceed:
                if criteria != "":
                    result.showResults(fileName, speaker, criteria)
                else:
                    result.showResults(fileName, speaker)
                proceed, criteria = checkProceeding(speaker)

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
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités!")
        else:
            result = Results(fileName)

            proceed = False
            while not proceed:
                if criteria != "":
                    result.showResults(fileName, speaker, criteria)
                else:
                    result.showResults(fileName, speaker)
                proceed, criteria = checkProceeding(speaker)
        
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
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités!")
        else:
            result = Results(fileName)

            proceed = False
            while not proceed:
                if criteria != "":
                    result.showResults(fileName, speaker, criteria)
                else:
                    result.showResults(fileName, speaker)
                proceed, criteria = checkProceeding(speaker)

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
                speaker.talk("Impossible de trouver des offres pour les intrants souhaités!")
        else:
            result = Results(fileName)

            proceed = False
            while not proceed:
                if criteria != "":
                    result.showResults(fileName, speaker, criteria)
                else:
                    result.showResults(fileName, speaker)
                proceed, criteria = checkProceeding(speaker)
    
    else:
        if speaker.lang == 'en':
            speaker.talk("Sorry but we can't find the desired transport method provided!")
        elif speaker.lang == 'fr':
            speaker.talk("Désolé mais nous ne trouvons pas le moyen de transport souhaité fourni!")
