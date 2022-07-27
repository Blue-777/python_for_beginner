# 수직 정렬, 폭 조정, 위젯 사이의 여백 조절, 위젯 내부의 여백 조절 
from tkinter import *
window = Tk()

btnList = [None] * 10

for i in range(0, 10):
    btnList[i] = Button(window, text = "button" + str(i+1))

for btn in btnList:
    btn.pack(side = BOTTOM, fill = X, ipadx = 100, ipady = 30, pady = 10) # side = RIGHT -> 수평 정렬: RIGHT, LEFT / 수직 정렬: TOP, BOTTOM
    # fill = X. 폭 조정 -> 양 옆으로 
    # pady = 10. 픽셀 값. 위젯 사이의 여백 조절 -> 위 아래로
    # 위젯 내부 여백 조절: ipadx = 100 -> 가로, ipady = 30 -> 세로
    
window.mainloop()