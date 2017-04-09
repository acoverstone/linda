from command import Command
from ./speech import speech
import pygame.mixer
from pygame.mixer import Sound


class MusicCmd(Command):
	INSTRUCTIONS = ['music', 'song']
	def execute(self)
		speech.speak("What song would you like to play?")
		songs = ['better together']
		response = speech.takeInput()
		if(songs not in response)
			speech.speak("This song does not exist in the library.")
			execute(self)
			return

		pygame.mixer.init()
		better_together = Sound("../resources/music/better_together.wav")

		if("better together" in response)
			better_together.play()