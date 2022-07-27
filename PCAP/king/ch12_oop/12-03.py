# 의 기본: 기본  

## class declaration part ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self):
        self.color = "red"
        self.speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
        
## main code part ##
myCar1 = Car()
myCar2 = Car()

print("car1 color is %s, the current speed is %dkm."%(myCar1.color, myCar1.speed))
print("car2 color is %s, the current speed is %dkm."%(myCar2.color, myCar2.speed))

