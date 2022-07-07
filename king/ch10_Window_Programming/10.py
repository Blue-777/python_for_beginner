# practice ques

# 1
# from tkinter import *

# window = Tk()
# window.title("practice window")
# window.geometry("400x100")
# window.resizable(width = FALSE, height = FALSE)

# window.mainloop()

# 2
# myBtn = Button(window, text = "end python", fg = "red", command = func1)

# 3
# from tkinter import *
# window = Tk()

# btnList = [None] * 5

# for i in range(5):
#     btnList[i] = Button(window, text = "button" + str(i + 1))
    
# for btn in btnList:
#     btn.pack(side = TOP)
    
# window.mainloop()

# 4
# from tkinter import * 

# def myClick(event):
#     messagebox.showinfo("mouse", "mouse right button double clicked")
    
# window = Tk()
# window.bind("<Double-Button-3>", myClick)
# window.mainloop()

# 5 
# [프로그램 1]의 완성
from tkinter import * 
from time import * 

## 전역 변수 선언 부분 ##
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0

## 함수 선언 부분 ##
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def clickPrev():
    global num
    num -= 1 
    if num < 0:
        num = 8
    photo = PhotoImage(file = "gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기 ")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)
        
window.mainloop()