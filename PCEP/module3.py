# 5
# vals = [0, 1, 2]
# vals.insert(0,1)
# del vals[1]
# print(vals)

# 7
# my_list = [[0,1,2,3] for i in range(2)]
# #print(my_list[2][0])
# print(my_list)

# # 8
# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
# print(t)
# print(i)

# 9 
# my_list =[0 for i in range (1, 3)]

# 12
# my_list = [1,2,3,4]
# print(my_list[-3:-2])

# 13
# my_list = [3,1,-2]
# print(my_list[my_list[-1]]) # print(my_list[my_list[-1]]) = print(my_list[-2])
# print(my_list[-2])

#14
# my_list = [1, 2, 3]
# for v in range(len(my_list)): # my_list의 길이만큼 돌려라 = 3 // v = range(3) 0, 1, 2
#     my_list.insert(1, my_list[v]) # range(3) = 0, 1, 2 이므로 첫번째 것은 0, index 0 자리에 1을 3번 넣라
# print(my_list)

#15
# var = 1 
# while var < 10:
#     print("#")
#     var  =  var << 1
#     print(var)
    
# 0  0  0  0  0  0  0  0  0
#             1  0  0  0  0 << 3 -> 8

#18
# for v in range(3): # index 0번째때 한번 # 찍고
#     print(v)
# else: # 포문 나와서 한번 # 찍는다.
#     print("#")
    
#19
# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0,v) # 0번째에다가 순서대로 넣야함. 상세 설명은 밑에..
# print(my_list_2)

# [1]
# [2, 1]
# [3, 2, 1]
 