# Fully functional implementation of the class: 클라스의 완전한 작동 구현 

## class declaration part ##
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value
        
## main code part ##
myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "blue"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "yellow"
myCar3.speed = 0

myCar1.upSpeed(30)
print("car1 color is %s, the current speed is %dkm."%(myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("car2 color is %s, the current speed is %dkm."%(myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("car3 color is %s, the current speed is %dkm."%(myCar3.color, myCar3.speed))