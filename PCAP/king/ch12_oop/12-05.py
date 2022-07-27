# [프로그램 1]의 완성 

## class declaration ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
        
    def getName(self):
        return self.speed
        
    def getSpeed(self):
        return self.speed
             
## variable declaration part ##
car1, car2, = None, None

## main code part ##
car1 = Car("audi", 0)
car2 = Car("benz", 30)

print(" %s\'s current speed is %dkm."%(car1.getName(), car1.getSpeed()))
print("%s\'s, current speed is %dkm."%(car2.getName(), car2.getSpeed()))