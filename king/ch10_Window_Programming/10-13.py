# 마우스 이벤트 기본 처리
from tkinter import * 
from tkinter import messagebox

## function definition section ##
def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼 클릭됨") # .showinfo(타이틀, 바디 = 컨텐츠)


## main code section ##   
window = Tk()

window.bind("<Button-1>", clickLeft) # bind: 묶다. .bind(명령어, 함수)

window.mainloop()