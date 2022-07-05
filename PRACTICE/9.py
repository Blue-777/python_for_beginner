class Failure (Exception): # 클라스 구조: clsaa 자식함수_이름Failure(부모함수_이름Exception) -> 여기서 파이썬이 포함하고 있는 클라스가 (여기 들어감)
    
    def __init__(self, message): # __init__은 초기 함수
        self.message = message
        
    def __str__(self): # object 자체를 프린트할 때 __str__이 실행됨. 12, 13번째 라인 때문에 출력됨
        return  "out of order " #+ self.message 
    
try:
    print("turn on") # 무조건 실행됨
    raise Failure (" crash") # self.message여서 __str__의 out of order crash가 출력됨. 
except Failure as problem: # 객체를 만들어준것. as problem # 11번째 라인 때문에 실행됨
    print (problem)
else: 
    print ("success")
    
    
'''
#추가 예시 설명
class classA(): # 오프젝트화 시킨다 classA: 사람   a1: 앨리스 
    def __init__(self,message,name): # __함수이름__:기본적으로 클라스가 가진 속성! 오버라이딩 해서 쓴다고 함. 태어나자마자 가지고 나오는 옵션. 예) 애기가 울면서 나온다. -> 여기서 우는 옵션 // (message, name)를 클라스 안에 던져줄 수 있다. 46번째줄
        self.message=message
        self.name= name
        print('cry form init'+self.message+self.name)
    def eat(self): # 개발자가 만들어준 속성(__함수 이름__)의 "__"가 없음.
        print('i am eat from xxx')
    def __str__(self):
            return  "I'm human and your massege is "+self.message+self.name

def alice_send():
   print('i am send from function')

alice = classA(' 메롱 ','alice') # classA가 alice라는 생명을 불어 넣는다. alice = object(생명을 불어넣고 만들어진 놈)
alice.eat() # command
alice.eat()
print(alice)
park = classA(' 메롱ㅋㅋㅋㅋ ','park')
print(park)

alice_send()
a1 = a() '''