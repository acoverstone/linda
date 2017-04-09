from command import Command
import threading
import speech
import sys

class TimerCmd(Command):             #command for starting a timer
    INSTRUCTIONS = ['timer'] #list of keywords
    def execute(self):
        speech.speak("How long do you wish to set the timer for?")
        # Input must be in the form of ____ hour, ___ minute, _____ seconds
        response = speech.takeInput()

        understood = False

        while(not understood):
            if("hours" in response or "hour" in response or "minutes" in response or "minute" in response or "seconds" in response or "second" in response):
                speech.speak("Timer starting");
                understood = True
            else:
                 speech.speak("I'm sorry I did not understand that. Please answer by saying blank hours blank minutes or blank seconds.");
            
        
        # t = threading.Timer(5.0, hello)
        # t.start() 

def hello():
    speech.speak("beep beep beep beep")
    print "hello, world"

def parseTime(response):
    if "second" in response or "seconds" in response:
        
