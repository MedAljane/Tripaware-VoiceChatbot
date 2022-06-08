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


    def showResults(self, resfile, speaker, qu, criteria="TotalPrice"):
        if self.resultFile:

            if speaker.lang == 'en':
                if self.resultFile["MultipleStops"] and self.fileName in ["intermodalOffers.json", "shuttleBusOffers.json"]:
                    speaker.talk(qu, "Showing results...")
                    speaker.talk(qu, f"The best choice by {criteria} is:")
                    speaker.talk(qu, f"Company: {self.bestChoices[criteria]['Details'][0]['companyName']}.")
                    speaker.talk(qu, f"Total duration: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                    speaker.talk(qu, f"Departure: {self.bestChoices[criteria]['Departure']['Time']} from {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Arrival: {self.bestChoices[criteria]['Arriving']['Time']} at {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                    speaker.talk(qu, f"With a total price of: {self.bestChoices[criteria]['TotalPrice']} EUR.")
                
                elif self.resultFile["MultipleStops"]:
                    speaker.talk(qu, "Showing results...")
                    speaker.talk(qu, f"The best choice by {criteria} is:")
                    speaker.talk(qu, f"Company: {self.bestChoices[criteria]['Details'][0]['companyName']}.")
                    speaker.talk(qu, f"Vehicule details: {self.bestChoices[criteria]['Details'][0]['Vehicule']['comfort']}, with {self.bestChoices[criteria]['Details'][0]['Vehicule']['Seats']} seats.")
                    speaker.talk(qu, f"Total duration: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                    speaker.talk(qu, f"Departure: {self.bestChoices[criteria]['Departure']['Time']} from {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Arrival: {self.bestChoices[criteria]['Arriving']['Time']} at {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                    speaker.talk(qu, f"With a total price of: {self.bestChoices[criteria]['TotalPrice']} EUR.")
                
                else:
                    speaker.talk(qu, "Showing results...")
                    speaker.talk(qu, f"The best choice by {criteria} is:")
                    speaker.talk(qu, f"Company: {self.bestChoices[criteria]['Details']['companyName']}.")
                    speaker.talk(qu, f"Vehicule details: {self.bestChoices[criteria]['Details']['Vehicule']['comfort']}, with {self.bestChoices[criteria]['Details']['Vehicule']['Seats']} seats.")
                    speaker.talk(qu, f"Total duration: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                    speaker.talk(qu, f"Departure: {self.bestChoices[criteria]['Departure']['Time']} from {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Arrival: {self.bestChoices[criteria]['Arriving']['Time']} at {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                    speaker.talk(qu, f"With a total price of: {self.bestChoices[criteria]['TotalPrice']} EUR.")
                    
            if speaker.lang == 'fr':
                if self.resultFile["MultipleStops"] and self.fileName in ["intermodalOffers.json", "shuttleBusOffers.json"]:
                    speaker.talk(qu, "Affichage des résultats...")
                    speaker.talk(qu, f"Le meilleur choix selon {criteria} est:")
                    speaker.talk(qu, f"Société: {self.bestChoices[criteria]['Details'][0]['companyName']}.")
                    speaker.talk(qu, f"Durée totale: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                    speaker.talk(qu, f"Départ: {self.bestChoices[criteria]['Departure']['Time']} de {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Arrivée: {self.bestChoices[criteria]['Arriving']['Time']} à {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Avec un prix total de: {self.bestChoices[criteria]['TotalPrice']} EUR.")
                
                elif self.resultFile["MultipleStops"]:
                    speaker.talk(qu, "Affichage des résultats...")
                    speaker.talk(qu, f"Le meilleur choix selon {criteria} est:")
                    speaker.talk(qu, f"Société: {self.bestChoices[criteria]['Details'][0]['companyName']}.")
                    speaker.talk(qu, f"Détails du véhicule: {self.bestChoices[criteria]['Details'][0]['Vehicule']['comfort']}, avec {self.bestChoices[criteria]['Details'][ 0]['Véhicule']['Seats']} places.")
                    speaker.talk(qu, f"Durée totale: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                    speaker.talk(qu, f"Départ: {self.bestChoices[criteria]['Departure']['Time']} de {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Arrivée: {self.bestChoices[criteria]['Arriving']['Time']} à {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Avec un prix total de: {self.bestChoices[criteria]['TotalPrice']} EUR.")
                
                else:
                    speaker.talk(qu, "Affichage des résultats...")
                    speaker.talk(qu, f"Le meilleur choix selon {criteria} est:")
                    speaker.talk(qu, f"Entreprise: {self.bestChoices[criteria]['Details']['companyName']}.")
                    speaker.talk(qu, f"Détails du véhicule: {self.bestChoices[criteria]['Details']['Vehicule']['comfort']}, avec {self.bestChoices[criteria]['Details']['Vehicule' ]['Seats']} places.")
                    speaker.talk(qu, f"Durée totale: {round(self.bestChoices[criteria]['TotalDuration'])} minutes.")
                    speaker.talk(qu, f"Départ: {self.bestChoices[criteria]['Departure']['Time']} de {self.bestChoices[criteria]['Departure']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Arrivée: {self.bestChoices[criteria]['Arriving']['Time']} à {self.bestChoices[criteria]['Arriving']['stopPoint']['name']}.")
                    speaker.talk(qu, f"Avec un prix total de: {self.bestChoices[criteria]['TotalPrice']} EUR.")

        else:
            if speaker.lang == 'en':
                speaker.talk(qu, "Sorry but we can't find any result for the given method!")
            elif speaker.lang == 'fr':
                speaker.talk(qu, "Désolé mais nous ne trouvons aucun résultat pour la méthode donnée!")
