import json  # For manipulating JSON files
import os  # For manipulating os files and folders
from deep_translator import GoogleTranslator  # For translating
from word2number import w2n  # For converting number words to actual numbers
from dateutil.parser import parse  # For datetime parsing
from placeDetails import getDetails  # For place details
from voiceSetup import take_command
from datetime import datetime
from voiceSetup import talk

def validPassengerInput(passengerInput):
    
    if len(passengerInput) == 1 and passengerInput.isnumeric():
        return True
    else :
        return False


def getDate():
    # Taking the voice input for the date
    depDate = take_command()

    # Translating the input to english for the date parser
    depDate = GoogleTranslator(source='auto', target='en').translate(depDate)

    # Using the date parser to get the formatted date and time
    depDate = parse(depDate, fuzzy=True)

    return depDate


def getsSeveralDetails():

    depPlace = ""
    validPlace = False
    # Departure place input to get details
    talk("insert departure place please!")
    while not validPlace:
        depPlace = take_command()

        validPlace = getDetails(depPlace)

        if validPlace:
            pass
        else:
            talk("Please provide a valid departure place!")

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
    talk("insert destination place please!")
    while not validPlace:
        destPlace = take_command()

        validPlace = getDetails(destPlace)
        
        if validPlace:
            pass
        else:
            talk("Please provide a valid destination place!")

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

    talk("insert date of departure please!")
    depDate = getDate()

    validDate = False

    while not validDate:
        try:
            date = depDate.strftime("%Y-%m-%d")
            time = depDate.strftime("%H:%M")
            validDate = True
        except:
            talk("Insert a valid date please!")
            valid = False
            depDate = getDate()

    # input the passengers
    talk("insert number of passengers please!")
    passengers = take_command()

    while not validPassengerInput(passengers):
        talk("insert a valid number of passengers please!")
        passengers = take_command()

    return depDetails, arrDetails, date, time, passengers