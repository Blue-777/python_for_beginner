# readline() -> read exactly three lines only

inFp = None # input file
inStr = "" # read file

inFp = open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()