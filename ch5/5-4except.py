#Error types // 예외 처리 try..except..

#1. FileNotFoundError: 디렉터리 안에 없는 파일을 열려고 할때 
'''f = open("not exist file", 'r')'''

#2. ZeroDivisionError
'''4/0'''

#3. IndexError리스트 안에서 얻을 수 없는 값 호출 
'''a = [1, 2, 3]
a[4]'''

#try, except
'''try:
    4/0
except ZeroDivisionError as e:
    print(e)'''
    
#try .. else
try:
    f = open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
    
#try .. finally
'''f = open('foo.txt', 'r')
try:
    print('a')
finally:
    f.close()'''
    
#try .. except -> 오류 회피하기
#try문 내에서 FileNotFoundError가 발생할 경우 pass를 사용하여 오류를 회피 
'''try:
    f = open('not exist file', 'r')
except FileNotFoundError:
    pass'''
    
#오류 일부러 발생시키기
'''class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird): #상속받은 클라스에 함수를 재구현하는 것 = 메서드 오버라이딩
    pass

eagle = Eagle()
eagle.fly()'''

#메서드 오버라이딩
'''class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()'''

