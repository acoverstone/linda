from command import Command
import speech
from time import sleep

class TodoCmd(Command):
	INSTRUCTIONS = ["to do"]

	def execute(self,Screens):
		Screens.show_frame("TodoScreen")
		frame = Screens.getFrame()
		speech.speak("What would you like to do to your to do list?")
		response = speech.takeInput()

		if "add" in response:
			speech.speak("What would you like to add to your to do list?")
			add_response = speech.takeInput()

			with open("resources/todo.txt", "a") as myfile:
				myfile.write(add_response + "\n")

		elif "delete" in response:
			speech.speak("What would you like to delete from your to do list?")
			delete_response = speech.takeInput()

			f = open("resources/todo.txt", "r")
			lines = f.readlines()
			f.close()
			f = open("resources/todo.txt", "w")

			for line in lines:
				if delete_response not in line:
					f.write(line)

			f.close()

		elif "clear" in response:
			speech.speak("Are you sure you want to clear your to do list?")
			clear_response = speech.takeInput()

			if "yes" in clear_response:
				open("resources/todo.txt", "w").close()
			else:
				self.execute(Screens)
                                return

                elif "read" in response:
                        with open("resources/todo.txt") as f:
                                todo_list = f.read().splitlines()
                                frame.showList(todo_list)
                                Screens.update()
                                sleep(15)
##                                speech.speak(todo_list)

                else:
                        speech.speak("I'm sorry that command does not exist")
                        self.execute(Screens)
                        return
                Screens.show_frame("TitleScreen")
