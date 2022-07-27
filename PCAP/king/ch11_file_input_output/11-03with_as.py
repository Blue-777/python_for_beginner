# with~as -> does not need close()

with open("/Users/alicesuh/Documents/PCAP/king/ch11_file_input_output/11-01memo.py", "r") as inFp:
    inList = inFp.readlines()
    print(inList)