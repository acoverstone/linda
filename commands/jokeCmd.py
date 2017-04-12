from command import Command
from screens.jokeScreen import JokeScreen
import speech
from time import sleep

class JokeCmd(Command):             #command for telling jokes
    INSTRUCTIONS = ['joke','jokes'] #list of keywords
    def execute(self,Screens):              #filled in abstract execute method
        Screens.show_frame("JokeScreen")
        frame = Screens.getFrame()

        knock = tk.Label(self, text="Knock Knock", fg="white",bg="black",font=("Helvetica", 30))
        knock.place(relx=0.5,rely=0.15,anchor='center')
        Screens.update()

        speech.speak("Knock, Knock")
        response = speech.takeInput()
        if("there" not in response):
            speech.speak("the correct response is, who's there.")
            knock.destroy()
            self.execute(Screens)
            return

        response1 = tk.Label(self, text="Who", fg="white",bg="black",font=("Helvetica", 30))
        response1.place(relx=0.5,rely=0.2,anchor='center')

        speech.speak("who");
        frame.response1()
        Screens.update()
        response = speech.takeInput();
        if("who" not in response):
            speech.speak("the correct response is, who who.")
            knock.destroy()
            response1.destroy()
            frame.clearScreen()
            self.execute(Screens)
            return
        frame.response2()

        response2 = tk.Label(self, text="Is there an owl in here? LOL", fg="white",bg="black",font=("Helvetica", 30))
        response2.place(relx=0.5,rely=0.3,anchor='center')

        Screens.update()
        speech.speak("Is there an owl in here? LOL")
        sleep(5)
        frame.clearScreen()
        Screens.show_frame("TitleScreen")
