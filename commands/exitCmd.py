from command import Command
import speech
import sys

class ExitCmd(Command):             #command for program termination
    INSTRUCTIONS = ['exit','quit', 'terminate'] #list of keywords
    def execute(self):              #filled in abstract execute method
        speech.speak("Now terminating.");
        sys.exit()
