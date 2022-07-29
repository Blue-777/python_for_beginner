# change image to black and white(completion of [program 1])

from tkinter import*
from tkinter.filedialog import * 
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

## function declaration part 
def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY
    
    window.geometry(str(width)+"x"+str(height))
    if canvas != None:
        canvas.destroy()
        
    canvas = Canvas(window, width = width, height = height)
    paper = PhotoImage(width = width, height = height)
    canvas.create_image((width/2, height/2), image = paper, state = 'normal')
    rgbString = ""
    rgbImage = img.convert('RGB')
    for i in range(0, height):
        tmpString = ""
        for k in range(0, width):
            r, b, g = rgbImage.getpixel((k, i))
            tmpString += "#%02x%02x%02x " %(r, g, b)     
            tmpString += "{" + tmpString + "} "
        paper.put(rgbString)
        canvas.pack()
        
def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY 
    readFp = askopenfilename(parent = window, filetypes = (("all drawing files", "*.jpg; *.jpeg; *.bmp; *.png; *.tif; *.gif"), ("all files", "*.*")))
    photo = Image.open(readFp).convert('RGB')
    oriX = photo.width
    oriY = photo.height 
    
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY
    
    if photo2 == None:
        return 
    saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG file", "*.jpg; *.jpeg"), ("all files", "*.*")))
    
    photo2.save(saveFp.name)
    
def func_exit():   
    exit()
    
def func_zoomin():   
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("zoom in", "Enter the magnification to enlarge", minvalue = 2, maxvalue = 4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX*scale), int(oriY*scale)))
    newX = photo2.width 
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_zoomout():  
    global window, canvas, paper, photo, photo2, oriX, oriY 
    scale = askinteger("zoom out", "Enter the magnification to reduce", minvalue = 2, maxvalue = 4)
    photo2 = photo.copy()
    photo2  = photo2.resize((int(oriX/scale), int(oriY/scale)))
    newX = photo2.width 
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_mirror1(): 
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_mirror2():  
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_rotatoe():     
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("rotate", "Enter the angle to rotate", minvalue = 0, maxvalue = 360)
    photo2 = photo.copy()
    photo2 = photo2.rotate(degree, expand = True)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_bright():  
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("brighten", "Enter the value(1.0~10.0)", minvalue = 1.0, maxvalue = 10.0)
    photo2 = photo.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_dark():    
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("darken", "Enter the value(0.0~1.0)", minvalue = 0.0, maxvalue = 1.0)
    photo2 = photo.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_blur():    
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)
    

def func_embo():    
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

def func_bw():    
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height 
    displayImage(photo2, newX, newY)

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