from command import Command
import speech
import os


class MusicCmd(Command):
        songs = ['better together']
	INSTRUCTIONS = ['music', 'song']
	def execute(self,Screens):
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
                            self.execute(self,Screens)
                            return


		if("better together" in response):
                        os.system("aplay resources/music/better_together.wav")
