import Tkinter as tk

class WeatherScreen(tk.Frame):
    def __init__(self, parent, controller):
        global label
        height = 2000
        width = 2000
        tk.Frame.__init__(self, parent,width=width,height=height,bg="black")
        self.controller = controller
        label = tk.Label(self, text="Weather Forecast", fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.5,rely=0.2,anchor='center')


    def today(self,day1):
        label = tk.Label(self, text=day1, fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.5,rely=0.25,anchor='center')
    def day2(self,day2):
        label = tk.Label(self, text=day2, fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.20,rely=0.40,anchor='center')
    def day3(self,day3):
        label = tk.Label(self, text=day3, fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.40,rely=0.40,anchor='center')
    def day4(self,day4):
        label = tk.Label(self, text=day4, fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.60,rely=0.40,anchor='center')
    def day5(self,day5):
        label = tk.Label(self, text=day5, fg="white",bg="black",font=("Helvetica", 30))
        label.place(relx=0.80,rely=0.40,anchor='center')
