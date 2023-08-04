from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text = time_string)

    date_string = strftime('%B %d, %Y')
    date_label.config(text = date_string)

    day_string = strftime('%A')
    day_label.config(text = day_string)

    time_label.after(1000, time)

time_label = Label(root, font=("space age", 50),  background = "black", foreground = "red")
time_label.pack(anchor = 'center')

day_label = Label(root, font=("space age", 25))
day_label.pack(anchor = 'center')

date_label = Label(root, font=("space age", 25))
date_label.pack(anchor = 'center')

time()
mainloop()