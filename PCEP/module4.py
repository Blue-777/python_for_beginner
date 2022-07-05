# 9
# def fun(inz = 2, out = 3 ): # in이 내장함수 이기 때문에 에라가 난다. 
#     return inz * out

# print(fun(3))

# 10
# tup = (1, ) + (1, ) # 이게 하나기 때문에 tup = (1, 1)이 됀다.
# print(tup)
# tup = tup + tup # 고로 tup + tup = (1, 1, 1, 1)이 됀다. 
# print(len(tup))
# print(tup)

# 12
# value = input("enter a value: ") # input argument는 다 str으로 받아주기 때문에 TypeError가 난다. 
# print(10/value)

# def fun(inp=2, out=3):
#     return inp *out

# print(fun(out=2))

# def fun(x):
#     x += 1
#     return x
# x = 2 
# x = fun(x + 1)
# print(x)

# def any():
#     print(var + 1, end = '')
    
# var = 1 
# any()
# print(var)

# def fun(x):
#     global y 
#     y = x * x
#     return y 

# fun(2)
# print(y)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else: 
#         return 
    
# print(fun(fun(2)) + 1)

# tup = (1, 2, 4, 8)
# tup = tup[1: -1]
# tup = tup[0]
# print(tup)

# 13
# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one'] # 'one'의 값은 'two'이므로 v에 'two' 값을 담아준다. 

# for k in range(len(dictionary)): # dictionary 의 length는 3이므로, for문을 3번 돌려준다. 
#     v = dictionary [v] # two: three, three: one, one: two -> 3번 돌려준 결과 v값은 two 이다. 
    
# print(v)

# 17
# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x-1) # f(x-1)이 f가 재귀함수 호출이다. 고로 3 + (3 - 1) + (2 - 1) = 6

# print(f(3))

# Test 
# 2
# def I():
#     s = 'abcdef'
#     for c in s[::2]:
#         yield c
# for x in I():
#          print(x, end=' ')

# 5
# my_list = [1, 2, 3]
# foo = list(map(lambda x: x**x, my_list))
# print(foo)

# 6
# from datetime import date
# date_1 = date(1992, 1, 16)
# date_2 = date(1991, 2, 5)
# print(date_1 - date_2)

# 7
# import calendar 
# print(calendar.weekheader(2)) # 갈호 안에 숫자는 아웃풋 하나 하나의 숫자를 나타낸다. 

# 8
# def o(p):
#         def q():
#             return'*' *p
#         return q
# r = o(1)
# s = o(2)
# print (r() + s())

# 12
# prime_numbers = [2]

# # convert list to bytearray
# byte_array = bytearray(prime_numbers)
# print(byte_array)

# # Output: bytearray(b'\x02\x03\x05\x07')

# 15 
# import os
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
# sizes = ['small', 'medium', 'large']
# for size in sizes:
#     os.mkdir(size)
# print(os.listdir())

# 16
# import calendar
# c = calendar.Calendar()
# for weekday in c.iterweekdays():
#     print(weekday, end="")

# 19
# def fun(x, y, z):
#     return x + 2 * y + 3 * z
# print(fun(0, z = 1, y = 3))