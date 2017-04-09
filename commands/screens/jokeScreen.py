import Tkinter as tk


class JokeScreen(tk.Frame):
    def __init__(self, parent, controller):
        global label
        height = 2000
        width = 2000
        tk.Frame.__init__(self, parent,width=width,height=height,bg="black")
        # root = tk.Tk()
        # w = 1500
        # h = 1500
        # root.geometry("%dx%d" % (w,h))
        # #root.overrideredirect(1)
        # self = tk.Frame(root, bg='black')
        # self.pack(fill='both', expand='yes')
        self.controller = controller
        label = tk.Label(self, text="Knock, Knock", fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.5,rely=0.1,anchor='center')


    def knock(self):
        label.destroy()
        knock = tk.Label(self, text="Knock Knock", fg="white",bg="black",font=("Helvetica", 30))
        knock.place(relx=0.5,rely=0.15,anchor='center')
    def response1(self):
        response1 = tk.Label(self, text="Who", fg="white",bg="black",font=("Helvetica", 30))
        response1.place(relx=0.5,rely=0.2,anchor='center')
    def response2(self):
        response2 = tk.Label(self, text="Is there an owl in here? LOL", fg="white",bg="black",font=("Helvetica", 30))
        response2.place(relx=0.5,rely=0.25,anchor='center')
