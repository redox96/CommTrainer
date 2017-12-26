from tkinter import *
from tkinter import filedialog

def file_save():
    f = asksaveasfilename(initialdir = "/",title = "Select file", mode='w', defaultextension=".txt")
    if f is None:
        return
    text2save = str(text.get(1.0, END))
    print (root.filename)
    f.write(text2save)
    f.close()
