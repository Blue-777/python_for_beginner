# method overriding 

## class declaration part 
class Car:
    speed = 0   # instance var\
        
    def upSpeed(self, value):
        self.speed += value
        
        print("current speed(super class): %d"%self.speed)
        
class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150:
            self.speed = 150
            
        print("current speed(subclass): %d"%self.speed)
        
class Truck(Car):
    pass

## var declaration part 
sedan1, truck1 = None, None

## main code part 
truck1 = Truck()
sedan1 = Sedan()

print("truck --> ", end = "")
truck1.upSpeed(200)

print("sedan --> ", end = "")
sedan1.upSpeed(200)
