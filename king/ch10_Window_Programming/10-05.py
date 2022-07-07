from tkinter import *
window = Tk()

# 깨알 정의 -> IDLE: 윈도우 통합 환경. 프로그램을 짤 때 도움을 주는 것 

button1 = Button(window, text = "end python", fg = "red", command = quit) # fg = for ground = 배경 앞 색상 

button1.pack()

window.mainloop()