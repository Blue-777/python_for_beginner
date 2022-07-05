# 2
# print("a", "b", "c", sep = "sep")
 
# 3
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
# print(fun(fun(2))) #* 재귀함수: fun(fun(2), fun(2) = 1 -> fun(1) = 2, 고로 답은 2

# 4
# dd = {"1":"0", "0":"1"}
# for x in dd.vals():
#     print(x, end="")

# 5
# def func(a, b):
#     return b ** a
# print(func(b=2, 2)) # a자리에 값이 있는것도 아니고, a 값이 없어서 error

# 6
# print(Hello, World!) # SyntaxError 

# 7. shallow copy
# nums = [1,2,3]
# vals = nums
# del vals[:]
# print(nums)
# print(vals)

# 8
# x = 1
# y = 2
# x, y, z = x, x, y 
# z, y, z = x, y, z
# print(x, y, z)

# 10 
# first = [[x for x in range(3)] for y in range(3)]
# for r in range(3):
#     for c in range(3):
#         if first[r][c] % 2 != 0:
#             print("#")

# 12. dictionary는 list와 같음. dictionary = {key : value}
# dct = {}
# dct['1'] = (1, 2) # dictionary['key'] = (values)
# dct['2'] = (2, 1)
# for x in dct.keys():
#     print(dct[x][1], end="")

# 13
# my_list = [x * x for x in range(5)] # 리스트: [표현식 for for문]
# def fun(first):
#     del first [first[2]] # 재귀함수: first[first[2]], first[2] = 4, first[4] = 16. 고로 my_list = [0, 1, 4, 9, 16]에서 16을 지움.
#     return first
# print(fun(my_list))

# 14
# x = int(input())
# y = int(input())
# x = x % y # 3 % 2 = 1
# x = x % y # 1 % 2 = 1
# y = y % x # 2 % 1 = 0
# print(y)

# 15
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1) # (0, 3-1) -> (0, 2-1) -> (0, 1-1) = (0, 0), 고로 71번째 줄에서 x값 0이 출력된다. 
# print(fun(0, 3))

# 17. ^ = Not 연산자: 다르면 1(false)이고, 같으면 0(true)
# a = 1
# b = 0
# a = a^b # 1
# b = a^b # 1
# a = a^b # 0
# print(a, b) 

# 21
# x = float(input())
# y = float(input())
# print(y**(1/x)) # 4**1/2 = 2.0

# 22
# try:
#     print(5/0)
#     break # break는 loop안(for etc..)에서만 사용 가능하므로 try..except..에서 쓸 수 없다. -> error
# except:
#     print("Sorry")
# except (ValueError, ZeroDivisionError):
#     print("Too")

# 23
# tup = (1,2,4,8)
# tup = tup[-2:-1]
# print(tup) # output: (4,) -> 리스트가 결과값이 하나일 때 index를 어떤걸 해도 그 하나가 나옴
# tup = tup[-1]
# print(tup)

# 24
# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value)) # 0 / 1 = 0, Value = 0, length = 1 
# except valueError:
#     print("bad")
# except ZeroDivisionError:
#     print("very")
# except TypeError:
#     print("very very")
# except: 
#     print("boo")

# 25
# foo = (1,2,3)
# foo.index(0) # index는 0이 안돼기 때문에 ValueError

# 26
# first = [i for i in range(-1)] # range(#1, #2) -> 무조건 #2이 #1보다 커야함, 뒤 숫자가 작을 경우 []이 출력됨
# print(first)

# 27
# print(1//5 + 1/5)

# 28
# def function_1(a):
#     return None 
# def function_2(a):
#     return function_1(a) * function_1(a) # none = 공백, 공백끼리 곱하기 때문에 error, runtime error -> TypeError
# print(function_2(2))

# 30
# i = 0
# while i < i + 2: # i < i + 2 조건에서 벗어나지 못하기 때문에 무한 루프가 돈다. 
#     i += 1
#     print("*")
# else: 
#     print("*")

# 31
# my_list=[1,2]
# for v in range(2): # range 0, 1 -> index 역할을 함 
#     my_list.insert(-1, my_list[v]) # -1 위치에 0번째 인덱스 값인 1을 넣어준다. [1, 1, 2]. 그리고 -1 위치에 1번째 인덱스 값인 1을 넣어준다. [1, 1, 1, 2]
# print(my_list)

# 34
# z = 0
# y = 10
# x = y<z and z>y or y>z and z<y 
# print(x)

# 35. shallow copy
# nums = [1,2,3]
# vals = nums
# print(nums)
# print(vals)
