from command import Command
import speech
import sys

class ExitCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['exit','quit', 'terminate'] #list of keywords
    def execute(self,Screens):              #filled in abstract execute method
        speech.speak("Now terminating.");
        sys.exit()
