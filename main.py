import snowboydecoder
import sys
import signal
import speech

from commands.weatherCmd import WeatherCmd


def controlLoop():
        speech.speak('Hi. How can I help you?')
        
        commandString = speech.takeInput()
        commands = [WeatherCmd()]
        for cmd in commands:
            cmd.decode(commandString)
