def f(a,b):
    return b(b) #error b(b)

print(f(lambda x:  x + 1, 0))