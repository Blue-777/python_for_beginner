# c:/doit/memo.py
import sys
import os 

option = sys.argv[1]
file_name = sys.argv[2]
#print(sys.argv[1]) #terminal에 python3 5-6.py you need python 이라고  칠때 5-6.py you need python이 arvg[#]로 불러짐
#print(option)

if option == '-a':
    memo = sys.argv[3]
    f = open(sys.argv[2], 'a')
    f.write(memo)
    f.write('\n')
    f.close() 
elif option == '-v':
    f = open(file_name)
    memo = f.read()
    f.close()
    print(memo)
elif option == '-del':
    os.remove(file_name)
    print("well removed, " + file_name)