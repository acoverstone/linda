import Tkinter as tk
import time

from commands.screens.jokeScreen import JokeScreen
from commands.screens.weatherScreen import WeatherScreen

class Screens(tk.Tk):
    def __init__(self, *args, **kwargs):
        global frame
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WeatherScreen, JokeScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("JokeScreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_frame(self):
        return frame
        
    def knockknockjoke(self):
        frame.knock()
        frame.response1()
        frame.response2()
