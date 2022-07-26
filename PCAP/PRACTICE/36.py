def power(a):
    def internal(x):
        return x**a;
    
    return internal 

cube = power(3)
print(cube(2))

