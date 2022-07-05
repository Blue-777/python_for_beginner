# 메뉴의 생성
from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "open")
fileMenu.add_separator()
fileMenu.add_command(label = "end")

window.mainloop()