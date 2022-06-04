from voiceSetup import Speaker
from random import choice
import json


class Results:
    
    global bestChoices
    global resultFile
    global fileName

    def bestChoice(obj, crit):
        bestCh = obj[choice(obj.keys())][0]

        for key in obj.keys():
            for element in obj[key]:
                if element[crit] < bestCh[crit]:
                    bestCh = element
        
        return bestCh


    def __init__(self,resfile):
        self.fileName = resfile
        # Getting list of best possibilities for each criteria
        f = open(resfile, "r")
        self.resultFile = json.load(f)
        f.close()

        def bestChoice(obj, crit):
            bestCh = obj[next(iter((obj.items())))[0]][0]

            for key in obj.keys():
                for element in obj[key]:
                    if element[crit] < bestCh[crit]:
                        bestCh = element
            
            return bestCh

        self.bestChoices = {
            "TotalCo2": bestChoice(self.resultFile["Carriers"], "TotalCo2") if bestChoice(self.resultFile["Carriers"], "TotalCo2") else "",
            "TotalDistance": bestChoice(self.resultFile["Carriers"], "TotalDistance") if bestChoice(self.resultFile["Carriers"], "TotalDistance") else "",
            "TotalDuration": bestChoice(self.resultFile["Carriers"], "TotalDuration") if bestChoice(self.resultFile["Carriers"], "TotalDuration") else "",
            "TotalPrice": bestChoice(self.resultFile["Carriers"], "TotalPrice") if bestChoice(self.resultFile["Carriers"], "TotalPrice") else ""
        }


    def showResults(self, resfile, speaker, criteria="TotalPrice"):
        if self.resultFile:
            if self.resultFile["MultipleStops"] and self.fileName in ["intermodalOffers.json", "shuttleBusOffers.json"]:
                speaker.talk("Showing results...")
                speaker.talk(f"The best choice by {criteria} is:")
                speaker.talk(f"Company: {self.bestChoices[criteria]['Details'][0]['companyName']}.")
                speaker.talk(f"Total duration: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                speaker.talk(f"Departure: {self.bestChoices[criteria]['Departure']['Time']} from {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                speaker.talk(f"Arrival: {self.bestChoices[criteria]['Arriving']['Time']} at {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                speaker.talk(f"With a total price of: {self.bestChoices[criteria]['TotalPrice']} EUR.")
            
            elif self.resultFile["MultipleStops"]:
                speaker.talk("Showing results...")
                speaker.talk(f"The best choice by {criteria} is:")
                speaker.talk(f"Company: {self.bestChoices[criteria]['Details'][0]['companyName']}.")
                speaker.talk(f"Vehicule details: {self.bestChoices[criteria]['Details'][0]['Vehicule']['comfort']}, with {self.bestChoices[criteria]['Details'][0]['Vehicule']['Seats']} seats.")
                speaker.talk(f"Total duration: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                speaker.talk(f"Departure: {self.bestChoices[criteria]['Departure']['Time']} from {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                speaker.talk(f"Arrival: {self.bestChoices[criteria]['Arriving']['Time']} at {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                speaker.talk(f"With a total price of: {self.bestChoices[criteria]['TotalPrice']} EUR.")
            
            else:
                speaker.talk("Showing results...")
                speaker.talk(f"The best choice by {criteria} is:")
                speaker.talk(f"Company: {self.bestChoices[criteria]['Details']['companyName']}.")
                speaker.talk(f"Vehicule details: {self.bestChoices[criteria]['Details']['Vehicule']['comfort']}, with {self.bestChoices[criteria]['Details']['Vehicule']['Seats']} seats.")
                speaker.talk(f"Total duration: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                speaker.talk(f"Departure: {self.bestChoices[criteria]['Departure']['Time']} from {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                speaker.talk(f"Arrival: {self.bestChoices[criteria]['Arriving']['Time']} at {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                speaker.talk(f"With a total price of: {self.bestChoices[criteria]['TotalPrice']} EUR.")

        else:
            speaker.talk("Sorry but we can't find any result for the given method!")
