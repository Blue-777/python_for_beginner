from tkinter import *
window = Tk()

button1 = Button(window, text = "button1")
button2 = Button(window, text = "button2")
button3 = Button(window, text = "button3")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

window.mainloop()