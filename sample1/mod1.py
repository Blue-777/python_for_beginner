# mod1.py 
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

print(__name__)

if __name__ == "mod1": #실행 파일 // 딴 데서 실행 
    print(add(1, 4))
    print(sub(4, 2))

if __name__ == "__main__": #import 할때 print를 생략하고 싶을 때 사용함// 요기서 실행
    print(add(2, 5))
    print(sub(3, 1))