# multi-threading
import threading 
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

th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()