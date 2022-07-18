# 1
# read() -> 파일의 내용 전체를 문자열로 리턴
# readline() -> 파일을 한 행씩 읽어 반환한다
# readlines() -> 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴
# write() -> 파일에 인자 값으로 준 스트링을 쓴다

2
# inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r", encoding = 'utf-8')

# inStr = inFp.readline()
# print(inStr, end = "")
    
# inFp.close()

# 3
# inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r", encoding = 'utf-8')

# inList = inFp.readlines()
# for inStr in inList:
#     print(inStr, end = "")
    
# inFp.close()

# 4
# os.path.exists() -> 파일이 없을때 오류가 발생하지 않게 한다. 

# 5
# inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r", encoding = 'utf-8')
# outFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "w", encoding = 'utf-8')


# inList = inFp.readlines() # 입력 파일의 모든 내용을 읽어 리스트로 담는다
# for inStr in inList:
#     outFp.write(inStr) # 리스트 요소를 하나씩 가져와 출력 파일에 쓴다

# 6 
# read() -> 파일의 내용을 처음부터 한 바이트씩 읽는다
# write() -> 파일에 한 바이트씩 쓴다. (반복문으로 무한 반복해야 함)

# 7
# 1) 파일 복사 = shutil.copy(소스 파일, 타깃 파일)
# 2) 디렉토리 복사 = shutil.copytree(소스 파일, 타깃 파일)
# 3) 디렉토리 생성 = os.mkdir(폴더명)
# 4) 디렉토리 삭제 = shutil.rmtree(폴더명)
# 5) 폴더 여부 확인 = os.path.exists(파일명 또는 폴더명)
# 6) 파일 삭제 = os.remove(파일명)

# 8
# 1) 없는 변수에 접근할 때 = NameError
# 2) 파일 처리에서 오류가 발생할 때 = IOError 
# 3) 실행에서 오류가 발생할 때 = RuntimeError
# 4) 딕셔너리에 키가 없을 때 = keyError

# 9
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