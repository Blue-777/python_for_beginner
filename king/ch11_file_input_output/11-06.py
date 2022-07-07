import os 

inFp = None
fName, inList, inStr = "", [], ""

fName = input("file name: ")

if os.path.exists(fName): # 파일이 없을 때 error가 발생하지 않게 함
    inFp = open(fName, "r")
    
    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end = "")
        
    inFp.close()
else:
    print("%s file not found" %fName)