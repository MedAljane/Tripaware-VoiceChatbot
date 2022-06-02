from datetime import datetime  # For time manipulation
from sevDetails import getsSeveralDetails
import requests  # For executing requests
from Results import Results
from voiceSetup import take_command
from voiceSetup import talk

# Services importing

def getTripAware(transport):
    vtc = ["vtc", "taxi", "vtc and taxi"]
    bus = ["bus", "navette", "bus et navette"]
    covoiturage = ["covoiturage", "co-voiturage", "voiturage"]
    intermodal = ["intermodal", "intermodale", "train"]

    if transport.lower() in vtc:
        from Services.useVtcTaxi import getVtcTaxi
        print("Welcome to VTC and Taxi reservation!")
        depDetails, arrDetails, date, time, passengers = getsSeveralDetails()
        talk("Getting offers, please wait...")
        fileName = getVtcTaxi(depDetails, arrDetails, date, time, passengers)

        if fileName == False:
            talk("Can't find offers for the desired inputs!")
        else:
            result = Results(fileName)
            result.showResults(fileName)
    
    elif transport.lower() in bus:
        from Services.useShuttleBus import getShuttleBus
        print("Welcome to navette and bus reservation!")
        depDetails, arrDetails, date, time, passengers = getsSeveralDetails()
        talk("Getting offers, please wait...")
        fileName = getShuttleBus(depDetails, arrDetails, date, time, passengers)

        if fileName == False:
            talk("Can't find offers for the desired inputs!")
        else:
            result = Results(fileName)
            result.showResults(fileName)
        
    elif transport.lower() in covoiturage:
        from Services.useCarpooling import getCarpooling
        print("Welcome to co-voiturage reservation!")
        depDetails, arrDetails, date, time, passengers = getsSeveralDetails()
        talk("Getting offers, please wait...")
        fileName = getCarpooling(depDetails, arrDetails, date, time, passengers)

        if fileName == False:
            talk("Can't find offers for the desired inputs!")
        else:
            result = Results(fileName)
            result.showResults(fileName)

    elif transport.lower() in intermodal:
        from Services.useIntermodal import getIntermodal
        print("Welcome to intermodal reservation!")
        depDetails, arrDetails, date, time, passengers = getsSeveralDetails()
        talk("Getting offers, please wait...")
        fileName = getIntermodal(depDetails, arrDetails, date, time, passengers)

        if fileName == False:
            talk("Can't find offers for the desired inputs!")
        else:
            result = Results(fileName)
            result.showResults(fileName)
    
    else:
        talk("Sorry but we can't find the desired transport method provided!")


talk("insert transport method please!")
transportMethod = take_command()

getTripAware(transportMethod)
