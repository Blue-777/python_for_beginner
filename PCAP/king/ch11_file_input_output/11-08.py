# duplicate or copy file 

inFp, outFp = None, None
inStr = ""

inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py","r")
outFp = open("alice1.txt","w") # 없는 파일 이름을 쓰면 파일이 새로 생기면서 그 내용이 통째로 복사됨 

inList = inFp.readlines() # 파일의 내용을 통째로 읽음
for inStr in inList:
    outFp.writelines(inStr) # 파일의 내용을 한 줄씩 배껴옴
    
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사 되었음---")