import json  # For manipulating JSON files
import os  # For manipulating os files and folders
from deep_translator import GoogleTranslator  # For translating
from word2number import w2n  # For converting number words to actual numbers
from dateutil.parser import parse  # For datetime parsing
from Tripaware.placeDetails import getDetails  # For place details
from datetime import datetime
from voiceSetup import Speaker

def validPassengerInput(passengerInput):
    
    if len(passengerInput) == 1 and passengerInput.isnumeric():
        return True
    else :
        return False


def getDate(speaker):
    # Taking the voice input for the date
    depDate = speaker.take_command()

    # Translating the input to english for the date parser
    depDate = GoogleTranslator(source='auto', target='en').translate(depDate)

    # Using the date parser to get the formatted date and time
    depDate = parse(depDate, fuzzy=True)

    return depDate


def getsSeveralDetails(speaker):

    depPlace = ""
    validPlace = False
    
    # Departure place input to get details
    if speaker.lang == 'en':
        speaker.talk("insert departure place please!")
    elif speaker.lang == 'fr':
        speaker.talk("insérez le lieu de départ s'il vous plait!")

    while not validPlace:
        depPlace = speaker.take_command()

        validPlace = getDetails(depPlace)

        if validPlace:
            pass
        else:
            if speaker.lang == 'en':
                speaker.talk("Please provide a valid departure place!")
            elif speaker.lang == 'fr':
                speaker.talk("Veuillez indiquer un lieu de départ valide!")

    f = open("placeDetails.json", "r")
    pDet = json.load(f)

    # Getting the code of the departure place
    if pDet["coordsFetch"]["result"]["place_codes"]["code"]:
        dep_code = pDet["coordsFetch"]["result"]["place_codes"]["code"]
    else:
        dep_code = ""

    # Filling the departure details
    depDetails = {
            "code_dep":dep_code,
            "id":pDet["idFetch"]["place_id"],
            "latitude":pDet["coordsFetch"]["result"]["geometry"]["location"]["lat"],
            "longitude":pDet["coordsFetch"]["result"]["geometry"]["location"]["lng"],
            "name":pDet["coordsFetch"]["result"]["name"],
            "address":pDet["coordsFetch"]["result"]["formatted_address"]
        }
    f.close()
    os.remove("placeDetails.json")

    destPlace = ""
    validPlace = False

    # Destination place input to get details
    if speaker.lang == 'en':
        speaker.talk("insert destination place please!")
    elif speaker.lang == 'fr':
        speaker.talk("insérer le lieu de destination s'il vous plait!")
        
    while not validPlace:
        destPlace = speaker.take_command()

        validPlace = getDetails(destPlace)
        
        if validPlace:
            pass
        else:
            if speaker.lang == 'en':
                speaker.talk("Please provide a valid destination place!")
            elif speaker.lang == 'fr':
                speaker.talk("Veuillez fournir un lieu de destination valide!")

    f = open("placeDetails.json", "r")
    pDet = json.load(f)

    # Getting the code of the destination place
    if pDet["coordsFetch"]["result"]["place_codes"]["code"]:
        dest_code = pDet["coordsFetch"]["result"]["place_codes"]["code"]
    else:
        dest_code = ""

    # Filling the departure details
    arrDetails = {
            "code_arr":dest_code,
            "id":pDet["idFetch"]["place_id"],
            "latitude":pDet["coordsFetch"]["result"]["geometry"]["location"]["lat"],
            "longitude":pDet["coordsFetch"]["result"]["geometry"]["location"]["lng"],
            "name":pDet["idFetch"]["structured_formatting"]["main_text"],
            "address":pDet["coordsFetch"]["result"]["formatted_address"],
            "addressLine1":pDet["idFetch"]["terms"][-1]["value"],
            "addressLine2":pDet["idFetch"]["terms"][-1]["value"]
        }
    f.close()
    os.remove("placeDetails.json")

    # Filling the departure date
    if speaker.lang == 'en':
        speaker.talk("insert date of departure please!")
    elif speaker.lang == 'fr':
        speaker.talk("insérez la date de départ s'il vous plait!")

    depDate = getDate(speaker)

    validDate = False

    while not validDate:
        try:
            date = depDate.strftime("%Y-%m-%d")
            time = depDate.strftime("%H:%M")
            validDate = True
        except:
            if speaker.lang == 'en':
                speaker.talk("Insert a valid date please!")
            elif speaker.lang == 'fr':
                speaker.talk("Insérez une date valide s'il vous plait!")
            valid = False
            depDate = getDate()

    # input the passengers
    if speaker.lang == 'en':
        speaker.talk("insert number of passengers please!")
    elif speaker.lang == 'fr':
        speaker.talk("insérez le nombre de passagers s'il vous plait!")
    passengers = speaker.take_command()

    while not validPassengerInput(passengers):
        if speaker.lang == 'en':
            speaker.talk("insert a valid number of passengers please!")
        elif speaker.lang == 'fr':
            speaker.talk("insérez un nombre valide de passagers s'il vous plait!")
        passengers = speaker.take_command()

    return depDetails, arrDetails, date, time, passengers