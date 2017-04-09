from command import Command
import threading
import speech
import sys

class TimerCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['timer'] #list of keywords
    def execute(self):              #filled in abstract execute method
        t = threading.Timer(5.0, hello)
        t.start() # after 30 seconds, "hello, world" will be printed

def hello():
    speech.speak("beep beep beep beep")
    print "hello, world"

    
