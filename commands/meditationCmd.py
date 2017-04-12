from command import Command
import speech
import os
import random


class MeditationCmd(Command):

    INSTRUCTIONS = ['meditate', 'meditation']
    def execute(self,Screens):
        found = False
        while not found:
            meditations = [0]
            numOfMeditations = len(meditations)
            playing = random.randint(0, numOfMeditations)

            for meditation in meditations:
                if meditation is playing:
                    found = True
                    if(playing == 0):
                        os.system("aplay resources/meditations/one.wav")
                        Screens.show_frame("TitleScreen")
            if(not found):
                speech.speak("There are no meditations in your library")
                self.execute(Screens)
                return
