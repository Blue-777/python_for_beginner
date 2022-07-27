# completion of [program2]
import turtle 
import random 

## class declaration part 
class Shape:    #super class
    myTurtle = None
    cx, cy = 0, 0   # center point of shape
    
    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')   # tutle produce 
        
    def setPen(self):   # random pen color and width
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)
        
    def drawShape(self):    # overriding from subclass
        pass 
    
class Rectangle(Shape):   #sub class
    width, height = [0]*2
    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        # draw rectangle 
        sx1, sy1, sx2, sy2 = [0]*4    # left top X, Y right bottom X, Y
        sx1 = self.cx - self.width/2
        sy1 = self.cy - self.height/2
        sx2 = self.cx + self.width/2
        sy2 = self.cy + self.height/2
        
        self.setPen()   # parents class method
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)
        
## function declaration part
def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()
    
## main code parts
turtle.title('Drawing an object-oriented rectangle with a turtle')
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()