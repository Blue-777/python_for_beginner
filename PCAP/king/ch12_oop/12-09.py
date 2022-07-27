# class' special method(__del__(), __repr__(), __add__(), __lt__(), __le__(), __gt__(), __ge__(), __eq__(), __ne__())

## class declaration part
class Line:
    length = 0
    def __init__(self, length):
        self.length = length
        print(self.length, 'length\'s line produced')
        
    def __del__(self):
        print(self.length, 'length\'s line deleted')
        
    def __repr__(self):
        return 'line\'s length: ' + str(self.length)
    
    def __add__(self, other):
        return self.length + other.length
    
    def __lt__(self, other):
        return self.length < other.length
    
    def __eq__(self, other):
        return self.length == other.length
    
    
## main code part
myLine1 = Line(100)
myLine2 = Line(200)

print(myLine1)

print('two line\'s length: ', myLine1 + myLine2)

if myLine1 < myLine2:
    print('line2 is longer')
elif myLine1 == myLine2:
    print('two line\'s length are same')
else:
    print('idk')
    
del(myLine1)