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
from commands.reminderCmd import ReminderCmd
from commands.meditationCmd import MeditationCmd


Screens = Screens()
def controlLoop():
    gloabl Screens
        speech.speak('Hi, how can I help you?')
        Screens.show_frame("ListeningScreen")
        commandString = speech.takeInput()
        commands = [WeatherCmd(), JokeCmd(), ReminderCmd(), ExitCmd(), TimerCmd(), MusicCmd(), UpdateCmd(), TodoCmd(), MeditationCmd()]
        found = False

        for cmd in commands:
                if cmd.decode(commandString,Screens):
                        found = True
        if not found:
                speech.speak("I am sorry, I did not understand that command.")

def getScreens():
    global Screens
    return Screens
