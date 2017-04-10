from command import Command
import speech
import os
import sys

class UpdateCmd(Command):             #command for updating
    INSTRUCTIONS = ['update'] #list of keywords
    def execute(self,Screens):              #filled in abstract execute method
        os.system("git pull origin UpdateCmd")
        speech.speak("Pulled the newest version of code")
        os.system("python linda.py")
        sys.exit()
