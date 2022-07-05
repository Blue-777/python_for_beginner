# b = bytearray([97, 98])
# print(b)

# class A:
#     A = 0
#     def __init__(self):
#         pass
# a = A()
# print(hasattr(a, 'A'))

# print(10!='1' + '0')
# print('9'*3>'9'*9)

# class A:
#      def __init__(self):
#          pass
#      def f(self):
#          return 1
#      def g(self):
#          return self.f()
# a = A()
# print(a.g())

# print(__name__)

# def a(x):
#      def b():
#         return x + x
#      return b
# x = a('x')
# y = a('')
# print(x() + y())

# z = 2
# y = 1
# x = y < z or z > y and y > z or z < y
# print(x)

# def fun(par2, par1):
#     return par2 + par1
# print(fun(1, par1=2))

# d = {}
# d['2'] = [1, 2]
# d['1'] = [3, 4]
# print(d.keys())
# for x in d.keys():
#     print(d[x][1])
#     # print(x)

# my_string = "abcdef"
# def fun(s):
#    del s[2]
#    return s
# print(fun(list(my_string)))

# def fun(d, k, v):
#     d[k] = v
#     return v
# my_dictionary = {}
# print(fun(my_dictionary, '1', 'v'))

# x = """

# """
# print(len(x))

# import calendar
# c = calendar.Calendar(calendar.SUNDAY)
# for weekday in c.iterweekdays():
#      print(weekday, end=" ")

# d = {1: 0, 2: 1, 3: 2, 0: 1}
# x = 0
# for y in range(len(d)):
#     x = d[x]
#     print(x)

# x = "\""
# print(len(x))

class A:
     A = 1
     def __init__(self, v=2):
         self.v = v +A.A
         A.A += 1
     def set(self, v):
         self.v +=v
         A.A += 1
         return
a = A()
a.set(2)
print(a.A)