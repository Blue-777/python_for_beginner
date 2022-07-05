# mod2.py 
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 

if __name__ == "__main__":
    a = Math()
    print(a.solv(10))
    