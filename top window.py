from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")


def topwin():

    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    l2 = Label(top, text = "this is toplevel window")
    l2.pack()

    top.mainloop()


l = Label(root, text = "this is the root level")
btn = Button(root, text = "click here to open another window", command = topwin)

l.pack()
btn.pack()
root.mainloop()