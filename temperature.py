from queue import Queue
import requests
import json

def tempEN(speaker, qu):

    # Enter your API key here 
    api_key = "b8e909c7c126a848d7d7ea55ceeeeaad"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    speaker.talk(qu, "choose the city please")
    #City_départ = input("city Name : ") 
    City_départ=take_command(qu)

    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + City_départ +"&units=metric"

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 

    # json method of response object 
    # convert json format data into 
    # python format data 
    x = response.json() 

    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 

        # store the value of "main" 
        # key in variable y 
        y = x["main"] 

        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 

        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 

        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 

        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 

        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z 
        weather_description = z[0]["description"] 
        speaker.talk(qu, "the weather in "+ City_départ +  "  :")
        
        # print following values 
        speaker.talk(qu, " Temperature  = " +
                str(current_temperature) +" celsius "+
                "\n Atmospheric pressure  = " +
                str(current_pressure) +" hPa "+
                "\n Humidity = " +
                str(current_humidiy) +" % "
                "\n " +
                str(weather_description)
            ) 

    else: 
        speaker.talk(qu, "City Not Found ... Please Try Again ") 


def tempFR(qu):

    # Enter your API key here 
    api_key = "b8e909c7c126a848d7d7ea55ceeeeaad"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    speaker.talk(qu, "choisissez la ville s'il vous plait")

    City_départ = input("Non de la vile : ") 


    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + City_départ +"&units=metric"

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 

    # json method of response object 
    # convert json format data into 
    # python format data 
    x = response.json() 

    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 

        # store the value of "main" 
        # key in variable y 
        y = x["main"] 

        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 

        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 

        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 

        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 

        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z 
        weather_description = z[0]["description"] 
        print("la météo dans "+ City_départ + "  :")
        speaker.talk(qu, "la météo dans "+ City_départ +  "  :")
        
        splitter = SentenceSplitter(language='en')
        description = GoogleTranslator(target='fr').translate(str(weather_description))
        # print following values 
        print(" Température  = " +
                        str(current_temperature) +" °C "+
            "\n Pression atmosphérique  = " +
                        str(current_pressure) +" hPa "+
            "\n Humidité  = " +
                        str(current_humidiy) +" % "
            "\n  =====>>  " +
                        description) 
        
        speaker.talk(qu, " Température  = " +
                        str(current_temperature) +" degré celsius "+
            "\n Pression atmosphérique  = " +
                        str(current_pressure) +" hPa "+
            "\n Humidité  = " +
                        str(current_humidiy) +" % "
            "\n " +
                        description) 

    else: 
        print(" Ville introuvable ... Veuillez réessayer") 
        speaker.talk(qu, " Ville introuvable ... Veuillez réessayer ") 
