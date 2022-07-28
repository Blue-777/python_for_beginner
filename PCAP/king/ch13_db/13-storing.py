# Storing black and white photos in DB (흑백 사진을 DB에 저장하기)
from tkinter import *
import sqlite3

## function declaration part 
def loadImage(fname):   #raw --> DB
    global inImage, XSIZE, YSIZE
    con, cur = None, None 
    row, col, data, sql = 0, 0, 0, ''
    con = sqlite3.connect("C:\Users\Donge\Downloads\CookPython\\rawDB")   
    cur = con.cursor()
    fp = open(fname, 'rb')
    for row in range(0, XSIZE):
        for col in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            sql = "INSERT INTO rawTable VALUES(" + str(row) + "," + str(col) + "," + str(data) + ")"
            cur.execute(sql)

    fp.close()
    con.commit()
    con.close()

def loadDatabase():     # DB --> memory
    global inImage, XSIZE, YSIZE
    con, cur = None, None
    row, col, data = 0, 0, 0, 
    record = None   # a line red from Table
    con = sqlite3.connect("C:\Users\Donge\Downloads\CookPython\\rawDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM rawTable")
    # produce empty inImage 
    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = 0
            tmpList.append(data)
        inImage.append(tmpList)

    # Table --> inImage
    while(True):
        record == cur.fetchone()
        if record == None:
            break;
        row = record[0]; col = record[1]; data = record[2]
        inImage[row][col] = data

    con.close()

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x#%02x#%02x " %(data, data, data)   
        rgbString += "{" + tmpString + "}"
    paper.put(rgbString)

## global var declaration part
window, canvas, XSIZE, YSIZE = None, None, 256, 256
inImage = []    # 2D list(memory)

## main code part
if __name__ == "__main__":
    window = Tk()
    window.title("RAW-->DB")
    canvas = Canvas(window, height = XSIZE, width = YSIZE)
    paper = PhotoImage(width = XSIZE, height = YSIZE)
    canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

    # initial Table
    con = sqlite3.connect("C:\Users\Donge\Downloads\CookPython\\rawDB") 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS rawTable")
    cur.execute("CREATE TABLE rawTable(row int, col int, data int)")    # row, column, pixel value
    con.commit()
    con.close()

    filename = 'C:\Users\Donge\Downloads\CookPython\RAW'
    loadImage(filename)     # file --> DB
    loadDatabase()  # DB --> memory
    displayImage(inImage)   # memory --> screen

    canvas.pack()
    window.mainloop()