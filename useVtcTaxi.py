from Tripaware.Services.sortAndClassify import classifyByCarrier
from voiceSetup import Speaker
from queue import Queue
import requests
import json

def getVtcTaxi(depDet, arrDet, date, time, passengers, speaker, qu):
    url = "https://api.ozeroute.com/v1/transportation/vtc_taxi"

    payload = json.dumps({
            "departureLocation":depDet,
            "arrivingLocation":arrDet,
            "date":date,
            "time":time,
            "passengers":{
                "adults":passengers,
                "babies":"0",
                "children":"0",
                "total":passengers
            },
            "immediate":False,
            "goingsComings":False,
            "tripType":{
                "hour":0,
                "tripType":"DEFAULT"
            },
            "tripOptions":{}
        })

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://airportmobility.rem4u.com',
        'Referer': 'https://airportmobility.rem4u.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'X-Auth-Key': '-161575564571d1-Om2kRN7Okf62EXO8w26EH1tCJgnAQOP7D-',
        'X-Auth-Token': 'rh5wwFkS1pwGDz0eSoGXw8yaefecqj4jJLHrQk8qeLw=',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'timestamp': '1654153335043'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    
    if response == {} or response == []:
        return False
    elif response["errors"]:
        speaker.talk(qu, "API malfunction, try again later please!")
        return False
    elif response == "Error response, please try again":
        speaker.talk(qu, "Invalid response! API error...")
        return False
    elif response != {} or response != []:
        response = classifyByCarrier(response)
        if response == False:
            return False
    else:
        return False

    with open("vtcTaxiOffers.json", "w") as resultFile:
        json.dump(response, resultFile)
    
    return "vtcTaxiOffers.json"
