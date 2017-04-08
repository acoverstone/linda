import snowboydecoder
import sys
import signal
from commands import speech


from commands.weatherCmd import WeatherCmd
from commands.jokeCmd import JokeCmd
from commands.musicCmd import MusicCmd


def controlLoop():
        speech.speak('Hi. How can I help you?')
        
        commandString = speech.takeInput()
        commands = [WeatherCmd(), JokeCmd(), MusicCmd()]
        for cmd in commands:
            cmd.decode(commandString)
