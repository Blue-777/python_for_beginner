from tkinter import *
window = Tk()

photo = PhotoImage(file = "a.png")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()