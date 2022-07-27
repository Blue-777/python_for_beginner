# 마우스 이벤트 기본 처리 2
from tkinter import * 
from tkinter import messagebox

## function definition section ##
def clickImage(event):
    messagebox.showinfo("마우스", "토끼에게 마우스가 클릭됨")


## main code section ##   
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "gif/rabbit.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()