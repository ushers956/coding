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



    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height=3)


btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')



lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()