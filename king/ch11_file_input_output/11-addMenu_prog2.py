# Add a menu to a black and white photo

# 프로그램 2) 흑백 사진 출력
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os.path
import math 

## function declaration part 
def loadImage(fname):
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage, filename

    inImage = []
    fsize = os.path.getsize(fname)  # file size
    XSIZE = YSIZE = int(math.sqrt(fsize))   # 정방향으로 가정하고 크기 구함 
    
    fp = open(fname, 'rb')
    
    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
        
    fp.close()

def displayImage(image):
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage, filename
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x "% (data, data, data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)
    
def func_open():
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage, filename

    filename = askopenfilename(parent = window, filetypes = (("RAW file", "*.raw"), ("all files", "*.*")))
    
    if filename == '':  # 대화상자에서 취소를 눌렀으면 
        return
    
    if canvas != None:  # 기존에 열린적이 있으면 삭제 
        canvas.destroy()

    # file --> memory 
    loadImage(filename)

    window.geometry(str(XSIZE) + 'x' + str(YSIZE))   # window size
    canvas = Canvas(window, height = XSIZE, width = YSIZE)
    paper = PhotoImage(width = XSIZE, height = YSIZE)
    canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

    # memory --> screen
    displayImage(inImage)
    
    canvas.pack()
    
def func_exit():
    window.quit()
    window.destroy()
    
def brightPhoto():
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage, filename
    value = 0
    value = askinteger('brighten', 'enter value', minvalue = 1, maxvalue = 255)
    
    for i in range(0, XSIZE):
        for k in range(0, YSIZE):
            data = inImage[i][k] + value
            if data>255:
                newData = 255
            else:
                newData = data
            inImage[i][k] = newData
            
    displayImage(inImage)

def darkPhoto():
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage, filename
    value = 0
    value = askinteger('darken', 'enter value', minvalue = 1, maxvalue = 255)
    
    for i in range(0, XSIZE):
        for k in range(0, YSIZE):
            data = inImage[i][k] - value
            if data<0:
                newData = 0
            else:
                newData = data
            inImage[i][k] = newData
            
    displayImage(inImage)
    
def reversePhoto():
    global window, canvas, paper, filename, XSIZE, YSIZE, inImage, filename
    
    for i in range(0, XSIZE):
        for k in range(0, YSIZE):
            data = inImage[i][k] 
            newData = 255 - data
            inImage[i][k] = newData
            
    displayImage(inImage)

## global variable declaration part ##
window = None
canvas = None
XSIZE, YSIZE = 0, 0
inImage = []    # 2D list(memory)
filename = ''   # file name(global variable)

## main code part ##
if __name__ == "__main__":
    window = Tk()
    window.title("흑백 사진 보기(menu")

    # add menu
    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "file", menu = fileMenu)
    fileMenu.add_command(label = "open file", command = func_open)
    fileMenu.add_separator()
    fileMenu.add_command(label = "end program", command = func_exit)

    photoMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "photo effect", menu = photoMenu)
    photoMenu.add_command(label = "brighten", command = brightPhoto)
    photoMenu.add_command(label = "darken", command = darkPhoto)
    photoMenu.add_command(label = "reverse image", command = reversePhoto)

window.mainloop()
