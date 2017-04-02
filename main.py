import snowboydecoder
import sys
import signal
from commands import speech

from commands.exitCmd import ExitCmd
from commands.weatherCmd import WeatherCmd
from commands.jokeCmd import JokeCmd


def controlLoop():
        speech.speak('Hi. How can I help you?')
        
        commandString = speech.takeInput()
        commands = [WeatherCmd(), JokeCmd(), ExitCmd()]
        for cmd in commands:
            cmd.decode(commandString)
