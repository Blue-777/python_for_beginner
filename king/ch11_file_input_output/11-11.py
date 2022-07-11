# 윈도창의 작성 

from tkinter import *

## variable declaration part ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256

## main code part ##
window = Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)

canvas.pack()
window.mainloop()

# # 흰 종이 

paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# # RAW 사진 파일의 화면 출력 
# #   step 1: RAW 파일을 메모리(imImage)로 불러 들인다. 
# for i in range(0, XSIZE):
#     tmpList = []
#     for k in range(0, YSIZE):
#         data = int(ord(fp.read(1)))
#         tmpList.append(data)
#     inImage.append(tmpList)
    
    
# #   step 2: 메모리(InImage)를 윈도창에 출력하는 기능은 displayImage() 함수에 구현 
# rgbString = ""
# for i in range(0, XSIZE):
#     tmpString = ""
#     for k in range(0, YSIZE):
#         data = image[i][k]
#         tmpString += "#%02x%02x%02x "%(data, data, data) # x 뒤에 한 칸 공백 
#     rgbString += "{" + tmpString + "} " # } 뒤에 한 칸 공백 
# paper.put(rgbString)