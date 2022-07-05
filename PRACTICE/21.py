class Storage:
    def __init__(self):
        self.rack = 1
        
    # Insert the method = function here.
    def get(self):
        return self.rack # 무조전 self.___이렇게 써주면 global function 처럼 써줄 수 있음. self = 예) 축구 할때 친구(다른 선언문)랑 한 공(rack: variable)을 share 하는것임. 

stuff = Storage()
print(stuff.get())

