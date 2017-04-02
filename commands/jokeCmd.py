from command import Command

class JokeCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['joke','jokes'] #list of keywords
    def execute(self):              #filled in abstract execute method
        print("Knock Knock")
        #print("What did the pirate say on his 80th birthday?")
        #print("Aye Matey!")


jokeCmd = JokeCmd()
jokeCmd.decode("joke");
