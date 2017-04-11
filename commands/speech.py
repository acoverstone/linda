import pyaudio
import os
import speech_recognition as sr

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
        return command

def speak(input):
        command = "cd picopi/pico/tts/ && ./testtts '. " + input + "'| aplay --rate=16000 --channels=1 --format=S16_LE"
        print command
        os.system(command)
        os.system("cd ../../..")

