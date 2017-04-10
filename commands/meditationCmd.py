from command import Command
import speech
import os


class MeditationCmd(Command):
    meditations = ['one']
    INSTRUCTIONS = ['meditate', 'meditation']
    def execute(self,Screens):
        found = False
        while not found:
            speech.speeak("What number meditation do you want to play?")
            response = speech.takeInput()
            if "quit" in response:
                break
            for meditation in self.meditations:
                if meditation in response:
                    found = True
            if(not found):
                speech.speak("This meditation does not exist in the library.")
                self.execute(Screens)
                return
            if("one" in response):
                os.system("aplay resources/meditations/one.wav")