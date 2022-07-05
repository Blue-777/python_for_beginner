import time
#print(time.localtime(time.time()).tm_year)
#print(time.asctime(time.localtime(time.time())))
#print(time.ctime())
import time
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
