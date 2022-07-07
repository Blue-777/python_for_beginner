# 프로그램 1) 파일 암호화 및 암호 해독 

# variable declaration part
inFp, outFp = None, None
inStr, outStr = "", ""
i = 0
secu = 0

# main code part 
secuYN = input("choose one of them -> 1. encoding 2. interpret code: ")
inFname = input("input file name: ")
outFname = input("output file name: ")

if secuYN == "1":
    secu = 100
elif secuYN == "2":
    secu = -100

inFp = open(inFname, 'r', encoding ='utf-8')
outFp = open(outFname, 'w', encoding = 'utf-8')

while True: 
    inStr = inFp.readline()
    if not inStr:
        break 
    
    outStr = ""
    for i in range (0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + 2
        
    outFp.write(outStr)
    
outFp.close()
inFp.close()
print('%s --> %s transformation completed' %(inFname, outFname))
