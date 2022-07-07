# 프로그램 2) 흑백 사진 출력 

from mimetypes import init
from tkinter import *

def loadImage(fname):
    global image, XSIZE, YSIZE
    fp = open(fname, 'rb')
    
    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
        
    fp.close()

## function declaration part ##
def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        forString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " %(data, data, data)
        rgbString += "{" + tmpString + "}"
    paper.put(rgbString)

## global variable declaration part ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

## main code part ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# file --> memory
filename = 'address?????' ##
loadImage(filename)

# memory --> screen
displayImage(inImage)

canvas.pack()
window.mainloop()