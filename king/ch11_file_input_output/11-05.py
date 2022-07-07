# 유닉스(맥)/도스(윈도우) 명령어 type의 구현 -> 출력하는 프로그램 
# 유닉스(맥)/도스(윈도우): 터미널에서 직접 실행 하는거, 터미널 명령어 
# 셸: 유닉스(맥)/도스(윈도우)

inFp = None 

fName = input("")
inFp = open(fName, "r")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end = "")
    
inFp.close()