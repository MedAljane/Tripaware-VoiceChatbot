from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests
import re
import json 
import datetime

def getCorona(speaker, qu):
    today = datetime.date.today().strftime('%Y-%m-%d')
    try:
        if speaker.lang == "en":
            speaker.talk(qu, "choose the city please")
        elif speaker.lang =="fr":
            speaker.talk(qu, "Choisissez la ville s'il vous plait:")

        x=speaker.take_command(qu)

        link_DataCountry = json.load(open("countriesCodes.json", "r"))
        if x.lower() not in link_DataCountry.keys():
            raise Exception(x.lower())


        if speaker.lang == "en":
            speaker.talk(qu, "Getting cases, please wait...")
        elif speaker.lang =="fr":
            speaker.talk(qu, "Obtenir des cas, veuillez patienter...")

        soup = BeautifulSoup(requests.get(f"https://www.worldometers.info/coronavirus/news-block/news_main_updates.php?fd=lm_{today}&country={link_DataCountry[x.lower()]}&days_count=5").content, 'html.parser').findAll('button', {'class': 'btn btn-light date-btn'})
        
        dates_En = []
        cases_En = []
        for date in soup:
            c = date.find_next_sibling('div', {'class': 'newsdate_div'}).findChild('li', {'class': 'news_li'})
            cases_En.append(c.text[:c.text.index('in')].strip())
            dates_En.append(date.text.strip())    

        new_cases_En = []
        new_deaths_En = []

        for e in cases_En:
            if "new cases" in e and "new deaths" in e:
                new_cases_En.append(e.split('and')[0].strip())
                new_deaths_En.append(e.split('and')[1].strip())
            elif "new cases" in e:
                new_cases_En.append(e)
                new_deaths_En.append("No new deaths")
            elif "new deaths" in e:
                new_cases_En.append("No new cases")
                new_deaths_En.append(e)
            else:
                new_cases_En.append("No new cases")
                new_deaths_En.append("No new deaths")

        if speaker.lang == "fr":
            new_cases_Fr = [GoogleTranslator(source='en', target='fr').translate(e) for e in new_cases_En]
            new_deaths_Fr = [GoogleTranslator(source='en', target='fr').translate(e) for e in new_deaths_En]
            dates_Fr = [GoogleTranslator(source='en', target='fr').translate(e) for e in dates_En]
            return dates_Fr, new_cases_Fr, new_deaths_Fr
        
        return dates_En, new_cases_En, new_deaths_En
        
    except:
        raise Exception()
