# making file explorer
from tkinter import * 
import os
import os.path 

## function declaration part 
def clickListBox(evt):
    global currentDir, searchDirList
    if (dirListBox.curselection() == ()): # 다른 리스트 박스를 클릭할 때는 무시 
        return
    dirName = str(dirListBox.get(dirListBox.curselection())) # 클릭한 폴더명
    if dirName == 'parent folder':
        if len(searchDirList) == 1: 
            return 
        searchDirList.pop()
    else:
        searchDirList.append(currentDir + dirName + '/')   # 검색 리스트에 클릭한 폴더 추가 
    fillListBox()
    
def fillListBox():
    global currentDir, searchDirList, dirLabel, dirListBox, fileLisBox
    dirListBox.delete(0, END)   # 폴더 리스트 박스를 비움
    fileListBox.delete(0, END)  # 파일 리스트 박스를 비움
    
    dirListBox.insert(END, "parent folder")
    currentDir = searchDirList[len(searchDirList)-1]
    dirLabel.configure(text = currentDir)
    folderList = os.listdir(currentDir)
    for item in folderList:
        if os.path.isdir(currentDir + item):
            dirListBox.insert(END, item)
        elif os.path.isfile(currentDir + item):
            fileListBox.insert(END, item)
            

## global varible declaration part 
window = None
searchDirList = ['/Users/alicesuh/Documents/PCAP']    # 중요 변수! 검색한 폴더 목록의 스택
currentDir = '/Users/alicesuh/Documents/PCAP'
dirLabel, dirListBox, fileListBox = None, None, None

## main code part
window = Tk()
window.title("folder and file lists")
window.geometry('300x500')

dirLabel = Label(window, text = currentDir)
dirLabel.pack()

dirListBox = Listbox(window)
dirListBox.pack(side = LEFT, fill = BOTH, expand = 1)
dirListBox.bind('<<ListboxSection>>', clickListBox)

fileListBox = Listbox(window)
fileListBox.pack(side = RIGHT, fill = BOTH, expand = 1)

fillListBox() # 초기에는 /Users/alicesuh/Documents/PCAP의 모든 폴더 목록 만들기 

window.mainloop()