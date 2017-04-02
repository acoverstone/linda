from command import Command
from ./speech import speech


class JokeCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['joke','jokes'] #list of keywords
    def execute(self):              #filled in abstract execute method
        speech.speak("Knock, Knock");
        response = speech.takeInput();
        if("there" not in response):
            speech.speak("the correct response is, who's there.")
            execute(self)
            return
        speech.speak("A herd");
        response = speech.takeInput();
        if("who" is not in response):
            speech.speak("the correct response is, A herd who.")
            execute(self)
            return
        speech.speak("A herd you were home, so I came on over")

        #print("What did the pirate say on his 80th birthday?")
        #print("Aye Matey!")
