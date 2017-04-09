from command import Command
import speech
import os

class UpdateCmd(Command):             #command for updating
    INSTRUCTIONS = ['update'] #list of keywords
    def execute(self):              #filled in abstract execute method
        os.system("git pull origin master")
        speech.speak("Pulling newest version of code")