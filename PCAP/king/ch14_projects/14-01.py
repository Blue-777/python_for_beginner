# menu implementation & function declaration 

from tkinter import*
from tkinter.filedialog import * 
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

## function declaration part 
def displayImage():     # implemented at code 14-02.py 
    pass

def func_open():    # implemented at code 14-02.py
    pass

def func_save():    # implemented at code 14-03.py 
    pass

def func_exit():   
    pass
    
def func_zoomin():   # implemented at code 14-04.py 
    pass

def func_zoomout():   # implemented at code 14-04.py
    pass 

def func_mirror1():  # implemented at code 14-05.py
    pass 

def func_mirror2():  # implemented at code 14-05.py
    pass

def func_rotatoe():     # implemented at code 14-06.py
    pass

def func_bright():  # implemented at code 14-07.py
    pass

def func_dark():    # implemented at code 14-07.py
    pass

def func_blur():    # implemented at code 14-08.py
    pass

def func_embo():    # implemented at code 14-08.py
    pass

def func_bw():    # implemented at code 14-08.py
    pass

## global var declaraiton part
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

## main code part
window = Tk()
window.geometry("250x250")
window.title("mini photoshop")

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "open file", command = func_open)
fileMenu.add_command(label = "save file", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "end program", command = func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "Image processing(1)", menu = image1Menu)
image1Menu.add_command(label = "zoom in", command = func_zoomin)
image1Menu.add_command(label = "zoom out", command = func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label = "upside down", command = func_mirror1)
image1Menu.add_command(label = "reverse left & right", command = func_mirror2)
image1Menu.add_command(label = "rotate", command = func_rotatoe)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "Image processing(2)", menu = image2Menu)
image2Menu.add_command(label = "brighten", command = func_bright)
image2Menu.add_command(label = "darken", command = func_dark)
image2Menu.add_separator()
image2Menu.add_command(label = "blurring", command = func_blur)
image2Menu.add_command(label = "embossingt", command = func_embo)
image2Menu.add_separator()
image2Menu.add_command(label = "black/white image", command = func_bw)

window.mainloop()