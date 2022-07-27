from tkinter import *
import os
import os.path

## 함수 선언 부분 ##
def clickListBox(evt):
    pass

def  fillListBox() :  # 항상 제일 검색한 폴더 리스트의 마지막 폴더(=현재 폴더)를 표시 
    pass
    
## 전역 변수 선언 부분 ##
window = None
searchDirList = ['/']  # 중요 변수! 검색한 폴더 목록의 스택
currentDir = '/'
dirLabel, dirListBox, fileListBox = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__" :
    window = Tk()
    window.title("폴더 및 파일 목록 보기")
    window.geometry('300x500')

    dirLabel = Label(window, text = currentDir)
    dirLabel.pack()
                               
    dirListBox = Listbox(window)
    dirListBox.pack(side = LEFT, fill = BOTH, expand = 1)
    dirListBox.bind('<<ListboxSelect>>', clickListBox)

    fileListBox = Listbox(window)
    fileListBox.pack(side = RIGHT, fill = BOTH, expand = 1)

    fillListBox()   # 초기엔 C:\\의 모든 폴더 목록을 만들기

    window.mainloop()
