# readline() -> read all lines in text file

inFp = None # input file
inStr = "" # read file

inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r")

while True: # while: 조건 안에서 무한 루프
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr, end = "")
    
inFp.close()