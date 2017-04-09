from command import Command
from screens.jokeScreen import JokeScreen
import speech
from time import sleep

class JokeCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['joke','jokes'] #list of keywords
    def execute(self,Screens):              #filled in abstract execute method
        Screens.show_frame("JokeScreen")
        frame = Screens.getFrame()
        speech.speak("Knock, Knock")
        response = speech.takeInput()
        if("there" not in response):
            speech.speak("the correct response is, who's there.")
            self.execute(Screens)
            return
        speech.speak("who");
        frame.response1()
        Screens.update()
        response = speech.takeInput();
        if("who" not in response):
            speech.speak("the correct response is, who who.")
            self.execute(Screens)
            return
        frame.response2()
        Screens.update()
        speech.speak("Is there an owl in here? LOL")

