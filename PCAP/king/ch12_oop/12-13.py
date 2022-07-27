# multi-processing

import multiprocessing 
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
if __name__ == "__main__":
    car1 = RacingCar('@car1')
    car2 = RacingCar('#car2')
    car3 = RacingCar('$car3')
    
    mp1 = multiprocessing.Process(target = car1.runCar) # multiprocessing.Process(target = 메서드 또는 함수, args = (매개변수))
    mp2 = multiprocessing.Process(target = car2.runCar)
    mp3 = multiprocessing.Process(target = car3.runCar)
    
    mp1.start() # 프로세스 시작
    mp2.start()
    mp3.start()
    
    mp1.join()  # 셍랙 가능하지만, 프로세스가 어떤 문제로 종료되지 않을때 작업이 끝나면 프로세스를 종료시켜 주는 역할을 함 
    mp2.join()
    mp3.join()