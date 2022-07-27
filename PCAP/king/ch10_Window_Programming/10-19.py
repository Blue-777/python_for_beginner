# 대화 상자의 생성과 사용 
from tkinter import * 
from tkinter.simpledialog import * # tkinter.simpledialog: Standard Tkinter input dialogs

window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "entered value")
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력 하세요", minvalue = 1, maxvalue = 6)

label1.configure(text = str(value))
window.mainloop()