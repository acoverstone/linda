from command import Command
import speech
import os
import random


class MeditationCmd(Command):
    meditations = [0]
    INSTRUCTIONS = ['meditate', 'meditation']
    def execute(self,Screens):
        found = False
        while not found:
            int numOfMeditations = len(meditations)
            int playing = random.randint(0, numOfMeditations)

            for meditation in self.meditations:
                if meditation is playing:
                    found = True
                    if(playing = 0):
                        os.system("aplay resources/meditations/one.wav")
            if(not found):
                speech.speak("There are no meditations in your library")
                self.execute(Screens)
                return
            