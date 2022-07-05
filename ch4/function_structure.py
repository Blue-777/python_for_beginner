#일반 함수: 입력값과 출력값이 있는 함수
'''def sum(a, b):
    return a + b

a = 3
b = 4
c = sum(a, b)
print(c)'''

#입력값이 없는 함수 
'''def say():
    return 'Hi'

a = say()
print(a)'''

#결과값이 없는 함수 
'''def sum(a, b):
    print("%d, %d의 합은 %d입니다."%(a, b, a + b))
a = sum(3, 4)
print(a)'''

#입력값도 결과값도 없는 함수 
def say():
    print('Hi')
say()