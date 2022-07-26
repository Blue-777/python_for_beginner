# 매개변수가 있는 생성자

## class declaration ##
class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
        
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
        
## main code part ##
myCar1 = Car("red", 30)
myCar2 = Car("blue", 60)

print("car1 color is %s, the current speed is %dkm."%(myCar1.color, myCar1.speed))
print("car2 color is %s, the current speed is %dkm."%(myCar2.color, myCar2.speed))

