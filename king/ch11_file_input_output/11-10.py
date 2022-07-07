# 이진 파일의 복사 

inFp, outFp = None, None 
inStr = ""

inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "rb")
outFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "wb")

while True: 
    inStr = inFp.read(1)
    if not inStr:
        break 
    outFp.write(inStr)
    
inFp.close()
outFp.close()
print("---이진 파일이 정상적으로 복사 되었음---")