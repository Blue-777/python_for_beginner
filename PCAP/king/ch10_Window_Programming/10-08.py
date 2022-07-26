from tkinter import *

## 메인 코드 부분 ##
window = Tk()

## 함수 선언 부분 ##
def myFunc():
    if var.get() == 1: 
        label1.configure(text = "python")
    elif var.get() == 2:
        label1.configure(text = "C++")
    else:
        label1.configure(text = "Java")
        
## 메인 코드 부분 ##
var = IntVar()
rb1 = Radiobutton(window, text = "python", variable = var, value = 1, command = myFunc) # Radiobutton = 동그란 체크 버튼, 멀티플 초이스 중에 하나만 선택 가능
rb2 = Radiobutton(window, text = "C++!", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java!", variable = var, value = 3, command = myFunc)

label1 = Label(window, text = "select language: ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()