from tkinter import * 
from tkinter.filedialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "selected file name")
label1.pack()

filename = askopenfilename(parent = window, filetypes = (("GIF file", "*.gif"), ("all files", "*.*")))

label1.configure(text = str(filename))

window.mainloop()