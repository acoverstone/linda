import Tkinter as tk

class MusicScreen(tk.Frame):
    def __init__(self, parent, controller):
        global label
        height = 2000
        width = 2000
        tk.Frame.__init__(self, parent,width=width,height=height,bg="black")
        self.controller = controller
        label = tk.Label(self, text="Music", fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.5,rely=0.2,anchor='center')
        photo = tk.PhotoImage(file = 'resources/images/music.gif')
        canvas = Canvas(width = 300, height = 200, bg = 'yellow')
        canvas.pack(expand = YES, fill = BOTH)
        gif = canvas.create_image(50, 10, image = gif1, anchor = NW)
        gif.image = photo
        #gif.place(relx=0.5,rely=0.3,anchor='center')
