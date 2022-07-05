from tkinter import *
from tkinter import messagebox

## 메인 코드 부분 ##
window = Tk()

## 함수 선언 부분 ##
def myFunc():
    if chk.get() == 0: # 0은 채크 안돼게 하면 off를 띄워라
        label1.configure(text = "click button off")
        print(chk.get())
    else:
        label1.configure(text = "click button on")
        print(chk.get())
        
## 메인 코드 부분 ##
chk = IntVar() # window program에서 int var을 가져다 씀. tkinter가 window program에서 가져다 씀
chk2 = IntVar()
cb1 = Checkbutton(window, text = "click it!", variable = chk, command = myFunc) # Checkbutton = 네모난 체크 박스, 체크 할 수 있다. 유무를 선택하는 경우에 사용. 여러개 체크 가능. 
cb2 = Checkbutton(window, text = "click it2!", variable = chk2, command = myFunc)
label1 = Label(window, text = "click button statuse: ", fg = "red")

cb1.pack()
cb2.pack()
label1.pack()

window.mainloop()