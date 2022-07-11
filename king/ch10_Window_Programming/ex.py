# 프로그램 2) 명화 감상하기
from tkinter import * 
from tkinter.filedialog import * 
from tkinter.simpledialog import *

def func_open():
    global photo, pLabel
    filename = askopenfilename(parent = window, filetypes = (("GIF file", "*.gif"), ("all files", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    print(photo.filename)
    pLabel.image = photo
    
def func_exit():
    window.quit()
    window.destroy()
   
def zoom(): 
    global photo, pLabel
    value = askinteger("확대배수", "확대배수 입력 하세요(2~8)", minvalue = 2, maxvalue = 8)
    photo = photo.zoom(value, value)
    pLabel.configure(image = photo)
    pLabel.image = photo 
    
def subsample(): 
    global photo, pLabel
    value = askinteger("축소배수", "축소배수 입력 하세요(2~8)", minvalue = 2, maxvalue = 8)
    photo = photo.subsample(value, value)
    pLabel.configure(image = photo)
    pLabel.image = photo 
    
    
window = Tk()
window.geometry("400x400")
window.title("appreciate famouse painting")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "file open", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "end program", command = func_exit)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "image effect", menu = fileMenu)
fileMenu.add_command(label = "zoom in", command = zoom)
fileMenu.add_separator()
fileMenu.add_command(label = "zoom out", command = subsample)

window.mainloop()