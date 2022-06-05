import speech_recognition as sr                 # For voice recognition
import pyttsx3                                  # For text to speech conversion

class Speaker:
    global lang
    global engine


    def __init__(self, language):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        if language == "fr":
            self.engine.setProperty('voice', self.engine.getProperty('voices')[2].id)
        elif language == "en":
            self.engine.setProperty('voice', self.engine.getProperty('voices')[0].id)
        self.engine.setProperty('rate', 222)
        self.engine.setProperty('volume', 1)
        self.lang = language
    
    def setLanguage(self, language):
        if language == "fr":
            self.engine.setProperty('voice', self.engine.getProperty('voices')[2].id)
            self.lang = language
        elif language == "en":
            self.engine.setProperty('voice', self.engine.getProperty('voices')[0].id)
            self.lang = language


    def talk(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait() 


    def take_command(self):
        if self.lang == 'fr':
            recognized = False
            while not recognized:
                with sr.Microphone() as source:
                    self.listener.adjust_for_ambient_noise(source, duration=1)
                    self.talk("J'ecoute...")
                    self.listener.pause_threshold = 1
                    audio = self.listener.listen(source)
            
                try:
                    self.talk("En train de reconnaître...") 
                    command = self.listener.recognize_google(audio, language ='fr')
                    print(f"Vous --->: {command}\n")
                    recognized = True
            
                except Exception as e:
                    self.talk("Impossible de reconnaître votre voix, veuillez réessayer...")
            
            return command

        elif self.lang == 'en':
            recognized = False
            while not recognized:
                with sr.Microphone() as source:
                    self.listener.adjust_for_ambient_noise(source, duration=1)
                    self.talk("Listening...")
                    self.listener.pause_threshold = 1
                    audio = self.listener.listen(source)
            
                try:
                    self.talk("Recognizing...") 
                    command = self.listener.recognize_google(audio, language ='en')
                    print(f"you --->: {command}\n")
                    recognized = True
            
                except Exception as e:
                    self.talk("Unable to Recognize your voice, try Again please...")
            
            return command