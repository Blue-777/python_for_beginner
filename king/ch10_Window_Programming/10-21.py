from tkinter import * 
from tkinter.filedialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "selected file name")
label1.pack()

saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG file", "*.jpg"), ("all files", "*.*")))

label1.configure(text = saveFp)
saveFp.close()

window.mainloop()

# jpg;*.jpeg is not a valid allowedFileType because it cannot be converted to a UTType
# 위에 쓴 에라남 