import speech_recognition as sr                 # For voice recognition
from queue import Queue
import pyttsx3                                  # For text to speech conversion

class Speaker:
    global lang
    global engine
    global avLanguages


    def __init__(self, language):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.avLanguages = {
            'french': [],
            'english': []
        }

        for voice in self.engine.getProperty('voices'):
            if 'english' in voice.name.lower():
                self.avLanguages["english"].append(voice)
            elif 'french' in voice.name.lower():
                self.avLanguages["french"].append(voice)

        if language == "fr":
            self.engine.setProperty('voice', self.avLanguages['french'][0].id)
        elif language == "en":
            self.engine.setProperty('voice', self.avLanguages['english'][0].id)

        self.engine.setProperty('rate', 200)
        self.engine.setProperty('volume', 1)
        self.lang = language
    
    def setLanguage(self, language):
        if language == "fr":
            self.engine.setProperty('voice', self.avLanguages['french'][0].id)
            self.lang = language
        elif language == "en":
            self.engine.setProperty('voice', self.avLanguages['english'][0].id)
            self.lang = language


    def talk(self, qu, text):
        qu.put(("Bot: ", text))
        if text in ["exit", "quitter", "quit", "cancel"]:
            exit()
        self.engine.say(text)
        self.engine.runAndWait() 


    def take_command(self, q):
        if self.lang == 'fr':
            recognized = False
            while not recognized:
                with sr.Microphone() as source:
                    self.listener.adjust_for_ambient_noise(source, duration=1)
                    self.talk(q, "J'ecoute...")
                    self.listener.pause_threshold = 1
                    audio = self.listener.listen(source)
            
                try:
                    self.talk(q, "En train de reconnaître...") 
                    command = self.listener.recognize_google(audio, language ='fr')
                    q.put(("Vous: " ,command))
                    recognized = True
            
                except Exception as e:
                    self.talk(q, "Impossible de reconnaître votre voix, veuillez réessayer...")
            
            return command

        elif self.lang == 'en':
            recognized = False
            while not recognized:
                with sr.Microphone() as source:
                    self.listener.adjust_for_ambient_noise(source, duration=1)
                    self.talk(q, "Listening...")
                    self.listener.pause_threshold = 1
                    audio = self.listener.listen(source)
            
                try:
                    self.talk(q, "Recognizing...") 
                    command = self.listener.recognize_google(audio, language ='en')
                    q.put(("you: ", command))
                    recognized = True
            
                except Exception as e:
                    self.talk(q, "Unable to Recognize your voice, try Again please...")
            
            return command