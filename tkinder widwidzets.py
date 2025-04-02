from tkinter import *
from datetime import date

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')


lbl = Label(text = "hey there", fg = "white", bg = "#072f5f", height=1, width = 300)

name_lbl = Label(text="full name", bg="#3895d3")
name_entry = Entry()

def display():



    name = name_entry.get()


    global message
    message = "welcome to the application \n todays date is: "
    greet = "hello"+name+"\n"