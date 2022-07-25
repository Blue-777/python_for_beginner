# multi-threading
import time

## class declaration part
class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name
        
    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + '~~ run \n'
            print(carStr, end = '')
            time.sleep(0.1)    # stop for 0.1 sec
            
## main code part
car1 = RacingCar('@car1')
car2 = RacingCar('#car2')
car3 = RacingCar('$car3')

car1.runCar()
car2.runCar()
car3.runCar()
