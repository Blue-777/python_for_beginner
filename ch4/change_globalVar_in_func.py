#함수 안에서 함수 밖의 변수를 변경하는 방법 

    #1. vrtest_return.py 
'''a = 1
def vartest(a):
    a = a + 1
    return a #요놈이 추가됨
    
a = vartest(a) # 대입하면 a가 vartest 함수의 결과값으로 봐뀐다. 
print(a)'''

    #2. vrtest_global.py 
a = 1
def vartest():
    global a #요놈이 추가됨
    a = a + 1
    
vartest()  
print(a)