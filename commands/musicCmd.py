from command import Command
from ./speech import speech
import pygame.mixer
from pygame.mixer import Sound


class MusicCmd(Command):
	INSTRUCTIONS = ['music', 'better', 'together']
	def execute(self)
		songs = ['better_together']
		response = speech.takeInput()
		if(songs not in response)
			speech.speak("This song does not exist in the library.")
			execute(self)
			return

		pygame.mixer.init()
		better_together = Sound("music/better_together.wav")

		if("better" in response)
			better_together.play()
		if("together" in response)
			better_together.play()