from voiceSetup import Speaker
from Tripaware.tripaware import getTripAware

sp = Speaker("en")

sp.talk("Please choose language! (English or French)")
sp.setLanguage("fr")
sp.talk("Veuillez choisir la langue! (Anglais ou français)")

language = sp.take_command()

validLanguage = False
while not validLanguage:
    if language.lower() in ["english","anglais","french","francais","français"]:
        if language.lower() in ["french","francais","français"]:
            sp.setLanguage('fr')
            language = 'fr'
        elif language.lower() in ['english', 'anglais']:
            sp.setLanguage('en')
            language = 'en'
        validLanguage = True
    else:
        sp.setLanguage("en")
        sp.talk("Language not supported! Please choose language between: English or French)")
        sp.setLanguage("fr")
        sp.talk("Langue non prise en charge ! Veuillez choisir la langue entre : anglais ou français)")
        
        language = sp.take_command()


if language == 'en':
    sp.talk("Insert the mean of transport please!")
elif language == 'fr':
    sp.talk("Insérez le moyen de transport s'il vous plaît!")


transportMethod = sp.take_command()

getTripAware(transportMethod, sp)