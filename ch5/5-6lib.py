#threading: 보통 1개의 프로세스는 1가지 일만 하지만, 
#thread를 이용하면 한 프로세스 내에서 2가지 또는 그 이상의 일을 동시에 수행하게 할 수 있다.

'''import threading
import time 

def say(msg):
    while True:
        time.sleep(1)
        print(msg)
        
for msg in ['you','need','python']:
    t = threading.Thread(target = say, args = (msg,))
    t.daemon = True
    t.start()
    
for i in range(100):
    time.sleep(0.1)
    print(i)'''
    
# thread_test.py
'''import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")'''