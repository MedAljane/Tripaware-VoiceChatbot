import requests
import json


def getDetails(place):

  # Getting the place ID from the autocomplete API
  idUrl = f"https://api.ozeroute.com/v1/place/autocomplete?input={place}"

  idpayload={}
  idHeaders = {
    'Accept': 'application/json',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://airportmobility.rem4u.com',
    'Referer': 'https://airportmobility.rem4u.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'X-Auth-Key': '-161575564571d1-Om2kRN7Okf62EXO8w26EH1tCJgnAQOP7D-',
    'X-Auth-Token': '4Z8a8br+kZD2Gw7j4SZFI1nlhbOmX6AurY9h9hYAIGk=',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timestamp': '1653119455665'
  }

  # API request
  idResponse = requests.request("GET", idUrl, headers=idHeaders, data=idpayload).json()


  # Getting the ID from the previous request to get the coordinates
  # from the details API
  try:
    ID = idResponse["predictions"][0]["place_id"]
  except IndexError:
    return False

  destination = idResponse["predictions"][0]

  # Setting the API with the place ID to get more details
  coordsUrl = f"https://api.ozeroute.com/v1/place/details?place_id={ID}&fields=name,address_components,types,geometry,formatted_address"

  coordsPayload={}
  coordsHeaders = {
    'Accept': 'application/json',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://airportmobility.rem4u.com',
    'Referer': 'https://airportmobility.rem4u.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'X-Auth-Key': '-161575564571d1-Om2kRN7Okf62EXO8w26EH1tCJgnAQOP7D-',
    'X-Auth-Token': 'PukohWy1p2Fkp9Ks8myi7eUz3JoiEoVBlgD0hM3oHd8=',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timestamp': '1653119623689'
  }

  # Coordinates details API request
  coordsResponse = requests.request("GET", coordsUrl, headers=coordsHeaders, data=coordsPayload).json()

  result = {
      "idFetch": destination,
      "coordsFetch": coordsResponse
  }

  with open('placeDetails.json', 'w') as json_file:
      json.dump(result, json_file)

  return True