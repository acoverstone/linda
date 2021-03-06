from command import Command
import speech
import os


class MusicCmd(Command):
    songs = ['better together']
    INSTRUCTIONS = ['music', 'song']
    def execute(self,Screens):
        Screens.show_frame("MusicScreen")
        frame = Screens.getFrame()
        speech.speak("What song would you like to play?")
        found = False
        while not found:
            response = speech.takeInput()
            if "quit" in response:
                break
            for song in self.songs:
                if song in response:
                    found = True
            if(not found):
                speech.speak("This song does not exist in the library.")
                self.execute(Screens)
                return
            if("better together" in response):
                frame.now_playing("Better Together by Jack Johnson")
                Screens.update()
                os.system("aplay resources/music/better_together.wav")
                Screens.show_frame("TitleScreen")
                Screens.update()
