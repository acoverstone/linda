from commands.screens.screens import Screens
from commands.screens.jokeScreen import JokeScreen
from time import sleep



Screens = Screens()
Screens.update()
cnt = 0;
while 1:
    if(cnt == 0):
        Screens.show_frame("JokeScreen")
        cnt = 1
    elif(cnt == 1):
        Screens.show_frame("WeatherScreen")
        cnt = 0
    Screens.update()
    Screens.update_idletasks()
    sleep(1)
    print("looping")
