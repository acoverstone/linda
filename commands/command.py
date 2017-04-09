import abc

class Command(object):
    def decode(self,input,args):    #method to check the speech input with our list of words
        Screens = args
        for instruction in self.INSTRUCTIONS:  #loops through all our instructions
            if instruction in input:    #checks if it needs to execute this command
                self.execute()       #executes the command

    @abc.abstractmethod
    def execute(self):
        #abstract function that holds all the logic for
        #    performing each command
        pass
