# 한 행씩 파일에 쓰기 

outFp = None 
outStr = ""

outFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py","w")

while True:
    outStr = input("내용 입력: ")
    if outStr != "": # 빈 값 들어가기 전까지 돌아라 -> 엔터 = 빈 값 // 공백 != 빈 값
        outFp.writelines(outStr +"\n")
    else: 
        break 
    
outFp.close()
print("---정상적으로 파일에 씀---")