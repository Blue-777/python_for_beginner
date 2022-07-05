# s = 'three'
# e = 0 
# try:
#     e = int(s)
# except ArithmeticError as e:
#    print("this is ", e)
   
# s = 'three'
# e = 0 
# try:
#     e = int(s)
# except ArithmeticError: #valueError나기 때문에 ArithmeticError 아님
#     e = 1
# except: #그래서 2가 프린트 됌
#     e = 2
# else:
#     e = 3
# print(e)

# print(int('three'))