import os
import sys

def search(dirname, myext): # dirname 하위 디렉토리 검색 .py 파일들을 검색
    try:
        filenames = os.listdir(dirname) #현재 디렉토리 목록가져오기 
         
        for filename in filenames: #디렉토리안에 파일가져오기 
           
            full_filename = os.path.join(dirname, filename) # 디렉토리을 포함한 전체 파일 이름 가져오기
            if os.path.isdir(full_filename): # 하위디록토리가 있을때까지 재기 호출하기 위해서 조건문처리함
                search(full_filename, myext)  # 재기호출 : 자기사진을호출
            else: # 최종 .py 포함한 조회 해서 프린트함
                ext = os.path.splitext(full_filename)[-1]  #.py 추출 
                if ext == myext: 
                    print(full_filename)
        #print()
        #print(filenames)  
    except PermissionError: #권항인 없을경우 패스 
        pass

for i in range(2, len(sys.argv)):
    search(sys.argv[1], sys.argv[i])
    #search(sys.argv[1], sys.argv[3]) # 위에 search 호출 
#print(sys.argv)











'''스승님 코딩'''
import os
import sys
## 첫번째 파라메터러 디렉토리 명을 받고 
## 두번째 파라미터로  확장장
## 확장자가 포함된 파일을 프린트 
def search(dirname,myext): # dirname 하위 디렉토리 검색 .py 파일들을 검색
    try:
        filenames = os.listdir(dirname) #현재 디렉토리 목록가져오기 
         
        for filename in filenames: #디렉토리안에 파일가져오기 
           
            full_filename = os.path.join(dirname, filename) # 디렉토리을 포함한 전체 파일 이름 가져오기
            if os.path.isdir(full_filename): # 하위디록토리가 있을때까지 재기 호출하기 위해서 조건문처리함
               # print(full_filename)
                search(full_filename,myext)  # 재기호출 : 자기사진을호출
               #pass
            else: # 최종 .py 포함한 조회 해서 프린트함
                ext = os.path.splitext(full_filename)[-1]  #.py 추출 
                #print('ext=',ext)
                if ext == myext: 
                    print(full_filename)
           
       # print(filenames)  
    except PermissionError: #권항인 없을경우 패스 
        pass

'''단순 노가다'''
#print("sys.argv[1] :",sys.argv[1]) ##특정 폴더

#print("sys.argv[2] :",sys.argv[2]) ## 특정 확장자 1

#print("sys.argv[3] :",sys.argv[3]) ## 특정 확장자 2

#print('sys.argv.count: ',sys.argv.count)

#print("This is the name of the script:", sys.argv[0])
#print("Number of arguments:", len(sys.argv))
#print("The arguments are:" , str(sys.argv))
 
 '''시니어급 응용'''
for i in range(2,len(sys.argv)):
    print(i)
    search(sys.argv[1],sys.argv[i]) # 위에 search 호출 root folder

'''마지막 index만 꺼내올 수 있게'''
#print(len(sys.argv))
#search(sys.argv[1],sys.argv[len(sys.argv)-1]) # 위에 search 호출 root folder


'''단순 노가다 코딩2'''
# if(len(sys.argv) > 3): #>3 = parameter가 3이 있을 경우 찍어라
#     search(sys.argv[1],sys.argv[3]) 

# if(len(sys.argv) > 4): #>3 = parameter가 3이 있을 경우 찍어라
#     search(sys.argv[1],sys.argv[4]) 

#print(sys.argv)