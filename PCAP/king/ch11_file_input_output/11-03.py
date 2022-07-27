# 한 번에 모두 읽어 들이기 

inFp = None
inList = ""

inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r")

inList = inFp.readlines()
print(inList)

inFp.close()
