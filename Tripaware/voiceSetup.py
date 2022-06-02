import speech_recognition as sr                 # For voice recognition
import pyttsx3                                  # For text to speech conversion


# Setting up the voice recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognized = False
    while not recognized:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            talk("Listening...")
            listener.pause_threshold = 1
            audio = listener.listen(source)
    
        try:
            talk("Recognizing...") 
            command = listener.recognize_google(audio, language ='fr')
            print(f"you --->: {command}\n")
            recognized = True
    
        except Exception as e:
            print(e)    
            print("Unable to Recognize your voice.")
     
    return command
