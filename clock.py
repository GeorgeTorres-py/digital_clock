from tkinter import Tk
from tkinter import Label
import sys
import time

master = Tk()
master.title("GT")


def get_time():
	timeVar = time.strftime('%I:%M:%S %p')
	clock.config(text=timeVar)
	clock.after(200, get_time)

clock = Label(master, font=("",85), bg="black", fg="white")
clock.pack()

get_time()



master.mainloop()
