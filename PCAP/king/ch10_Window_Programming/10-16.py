# 키보드 이벤트 기본 처리 
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event):
    messagebox.showinfo("keyboard event", "pressed key: " + repr(event.char)) # ch = repr 

## 메인 코드 부분 ##
window = Tk()

window.bind("<Key>", keyEvent)

window.mainloop()