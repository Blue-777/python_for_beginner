# 클라스 변수의 개념: 자동차가 몇 대 생산되었는지 확인 하는 코드 

## class declaration part 
class Car:
    color = ""  # instance var
    speed = 0   # instance var
    count = 0   # class var
    
    def __init__(self):
        self.speed = 0 
        Car.count += 1
        
## var declaration part 
myCar1, myCar2 = None, None

## main code part 
myCar1 = Car()
myCar1.speed = 30
myCar1.count = 20
print("car1\'s current speed is %dkm, number of produced cars are %d."%(myCar1.speed, myCar1.count))

myCar2 = Car()
myCar2.speed = 60
print("car2\'s current speed is %dkm, number of produced cars are %d."%(myCar2.speed, Car.count))
