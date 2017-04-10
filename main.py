import snowboydecoder
import sys
import signal
from commands import speech
from commands.screens.screens import Screens

from commands.exitCmd import ExitCmd
from commands.weatherCmd import WeatherCmd
from commands.jokeCmd import JokeCmd
from commands.timerCmd import TimerCmd
from commands.musicCmd import MusicCmd
from commands.updateCmd import UpdateCmd
from commands.todoCmd import TodoCmd

Screens = Screens()
def controlLoop():
        speech.speak('Hi. How can I help you?')
        commandString = speech.takeInput()
        commands = [WeatherCmd(), JokeCmd(), ExitCmd(), TimerCmd(), MusicCmd(), UpdateCmd(), TodoCmd()]
        for cmd in commands:
            cmd.decode(commandString,Screens)

def getScreens():
    global Screens
    return Screens
