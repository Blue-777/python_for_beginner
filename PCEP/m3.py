# 2
# class A:
#     X = 0
#     def __init__(self, v = 0):
#         self.Y = v
#         A.X += v

# a = A()
# b = A(1)
# c = A(2)
# print(a.X)
# print(b.Y)
# print(c.Y)

# 10
# class A:
#     def __init__(self,v):
#         self.__x = v + 1 #__ = private이라 manglo이다. 고로 class안에서만 쓸 수 있다. 

# a = A(0)
# print(a.__x)

# 13
# class A:
#     def __init__(self, v = 1):
#         self.v = v
#     def set (self, v):
#         self.v = v
#         return v 
# a = A()
# print(a.v + 1)


