from command import Command
from screens.jokeScreen import jokeScreen
from screens.weatherScreen import weatherScreen
#import speech


class JokeCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['joke','jokes'] #list of keywords
    command = "Joke"
    def execute(self):              #filled in abstract execute method
        Screen.show_frame("JokeScreen")
        speech.speak("Knock, Knock");
        response = speech.takeInput();
        if("there" not in response):
            speech.speak("the correct response is, who's there.")
            self.execute()
            return
        speech.speak("A herd");
        response = speech.takeInput();
        if("who" not in response):
            speech.speak("the correct response is, A herd who.")
            self.execute()
            return
        speech.speak("A herd you were home, so I came on over")
