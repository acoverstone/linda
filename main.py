import snowboydecoder
import sys
import signal
from commands import speech
from commands.screens.screens import Screens

from commands.exitCmd import ExitCmd
from commands.weatherCmd import WeatherCmd
from commands.jokeCmd import JokeCmd
from commands.timerCmd import TimerCmd


def controlLoop():
        speech.speak('Hi. How can I help you?')
        Screen = Screen()
        commandString = speech.takeInput()
        commands = [WeatherCmd(), JokeCmd(), ExitCmd(), TimerCmd()]
        for cmd in commands:
            cmd.decode(commandString,Screen)

        Screen.update_idletasks()
        Screen.update()
