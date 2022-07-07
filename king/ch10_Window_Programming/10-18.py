# 메뉴의 생성2
from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo("select menu", "select open menu")
    
def func_exit():
    window.quit()
    window.destroy()
    
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "open", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "end", command = func_exit)

window.mainloop()