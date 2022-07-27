# readlines()를 사용해 한 번에 모두 읽고 for 문을 사용해 리스트 내용을 하나씩 출력 

inFp = None
inList, inStr = [], ""

inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r")
            
inList = inFp.readlines()
for inStr in inList: # for: 값을 자유 자제로 쓰고 싶을 때
    print(inStr, end = "")
    
inFp.close()
