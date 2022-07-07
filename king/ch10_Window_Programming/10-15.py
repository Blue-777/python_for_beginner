# event 매개변수를 활용한 마우스 이벤트 처리 
from tkinter import * 

## 함수 선언 부분 ##
def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "mouse left button clicked on ("
    elif event.num == 3:
        txt += "mouse right button clicked on ("
    
    txt += str(event.y) + "," + str(event.x) + "), ok!!"
    label1.configure(text = txt)

## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")

label1 = Label(window, text = 'This part changed')

window.bind("<Button>", clickMouse)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()