# Implementing Paint with object-oriented application
from tkinter import *
import math 
import random

## class declaration part
class Shape:     # super class
    color, width = '', 0
    shX1, shY1, shX2, shY2 = [0]*4  # two points containing a shape
    def drawShape(self):    # abstract method
        raise NotImplementedError()
    
class Rectangle(Shape):     # subclass
    objects = None   # list of square segments = 사각형 선분 리스트 
    def __init__(self, x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()
        
    def __del__(self):  # Delete segment 4 of the rectangle
        for obj  in self.objects:
            canvas.delete(obj)
        
    def drawShape(self):    # Overriding by drawing a rectangle
        sx1 = self.shX1; sy1 = self.shY1; sx2 = self.shX2; sy2 = self.shY2
        squareList = []
        squareList.append(canvas.create_line(sx1, sy1, sx1, sy2,
                                            fill = self.color, width = self.width))
        squareList.append(canvas.create_line(sx1, sy2, sx2, sy2,
                                            fill = self.color, width = self.width))
        squareList.append(canvas.create_line(sx2, sy2, sx2, sy1,
                                            fill = self.color, width = self.width))
        squareList.append(canvas.create_line(sx2, sy1, sx2, sy2,
                                            fill = self.color, width = self.width))
        self.objects = squareList   # Put a list of segments (rectangles) into an object
    
class Circle(Shape):    # subclass
    objects = None
    def __init__(self, x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()
        
    def __del__(self):  # Circle deletes only 1 object
        canvas.delete(self.objects)
        
    def drawShape(self):    # Overriding with circular drawing
        sx1 = self.shX1; sy1 = self.shY1; sx2 = self.shX2; sy2 = self.shY2
        self.objects = canvas.create_oval(sx1, sy1, sx2, sy2, 
                                          outline = self.color, width = self.width)
        
## function declaration part
def getColor():     # random color select   
    r = random.randrange(16, 256)   # When converted to hexadecimal(16진수), 0 to A are excluded.
    g = random.randrange(16, 256)
    b = random.randrange(16, 256)
    return "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]   # Created in the form 'rrggbb'

def getWidth():     # Random pen thickness selection
    return random.randrange(1, 9)

## event function declaration part 
def startDrawRect(event):
    global x1, y1, x2, y2, shapes
    x1 = event.X
    y1 = event.y
    
def endDrawRect(event):
    global x1, y1, x2, y2, shapes
    x2 = event.x
    y2 = event.y
    rect = Rectangle(x1, y1, x2, y2, getColor(), getWidth())    # create Rectangle
    shapes.append(rect)
    
def startDrawCircle(event):
    global x1, y1, x2, y2, shapes
    x1 = event.x
    y1 = event.y
    
def endDrawCircle(event):
    global x1, y1, x2, y2, shapes 
    x2 = event.x
    y2 = event.y 
    cir = Circle(x1, y1, x2, y2, getColor(), getWidth()) # create Circle
    shapes.append(cir)  # Add to all shapes list
    
def deleteShape(event):     # Remove the last drawn shape
    global shapes 
    if len(shapes) != 0:    # Remove the last shape if there is a picture on the screen
        shp = shapes.pop()
        del(shp)
        
## global var declaration part 
shapes = []     # List of all figures drawn on the screen
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None     # X, Y of the two clicked points
        
## main code part 
if __name__=="__main__":
    window = Tk()
    window.title("oop paint board")
    canvas = Canvas(window, height = 300, width = 300)
    canvas.bind("<Button-1>", startDrawRect)
    canvas.bind("<ButtonRelease-1>", endDrawRect)
    canvas.bind("<Button-2>", deleteShape)
    canvas.bind("<Button-3>", startDrawCircle)
    canvas.bind("<ButtonRelease-3>", endDrawCircle)
    
    canvas.pack()
    window.mainloop()