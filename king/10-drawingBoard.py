# make drawing board
from tkinter import *
from tkinter.colorchooser import * 
from tkinter.simpledialog import *

## function declaration part ##
def mouseClick(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event):
    global x1, y1, x2, y2, penWidth, pencolor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width = penWidth, fill = penColor)
    
def getColor():
    global pencolor
    color = askcolor()
    penColor = color[1]
    
def getWidth():
    global penWidth
    penWidth = askinteger("line width", "input line width(1~10)", minvalue = 1, maxvalue = 10)
    
## global variable declaration part ##
window = None
canvas = None 
x1, y1, x2, y2 = None, None, None, None
penColor = 'black'
penWidth = 5

## main code part ##
if __name__=="__main__":
    window = Tk()
    window.title("drawing board similar program")
    canvas = Canvas(window, height = 300, width = 300)
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    canvas.pack()
    
    mainMenu = Menu(window)
    window.config(menu = mainMenu) 
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "setting", menu = fileMenu)
    fileMenu.add_command(label = "select line color", command = getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label = "select line width", command = getWidth)
    
    window.mainloop()