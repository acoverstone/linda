from command import Command
from ..speech import speech


class JokeCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['joke','jokes'] #list of keywords
    def execute(self):              #filled in abstract execute method
        speech.speak("Knock, Knock");
        response = speech.takeInput();
        speech.speak(response);
        #print("What did the pirate say on his 80th birthday?")
        #print("Aye Matey!")
