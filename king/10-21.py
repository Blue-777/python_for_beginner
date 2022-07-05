from tkinter import * 
from tkinter.filedialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "selected file name")
label1.pack()

saveFp = askopenfilename(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG file", "*.jpg;*.jpeg"), ("all files", "*.*")))

label1.configure(text = saveFp)
saveFp.close()

window.mainloop()