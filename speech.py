import pyaudio
import pyttsx
import speech_recognition as sr

from commands.weatherCmd import WeatherCmd
from commands.jokeCmd import JokeCmd

# obtain audio input from the microphone
def takeInput():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Say something!")
                audio = r.listen(source)
                print("Okay, now checking.")

        WIT_AI_KEY = "7BO32QHUGL7H4XU3HJTTA2EJH2KLHEMV"
        try:
                command = r.recognize_wit(audio, key=WIT_AI_KEY)
                print("You said: " + command)
        except sr.UnknownValueError:
                print("Wit.ai could not understand audio.")
        except sr.RequestError as e:
                print("Could not request results from wit.ai; {0}".format(e))


def controlLoop():
        ## Say 'How can I help you?' 
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        for voice in voices:
                engine.setProperty('voice', voice.id)
                print voice
        engine.setProperty('voice', 'en-us+f1')
        engine.say('Hi. How can I help you?')
        engine.runAndWait()

        
        takeInput()
        commands = [WeatherCmd() JokeCmd()]
        
        

        
