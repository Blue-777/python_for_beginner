# Q7 try..except..예외처리 & assert 뒤의 조건이 True가 아니면 AssertError 발생 시킴
def attic(x):
    assert x != 0
    return 1/x

def floor(x):
    try:
        attic(x)
    except:
        raise

try:
    x = attic (0)
except RuntimeError: #RuntimeError가 발생하면 -3을 찍어라
    x = -3
except: #다른 에라 발생시 -2를 찍어라// 여기선 AssertionError가 발생하므로 결과값이 -2임
    x = -2
else: #에라가 안날 경우에 -1을 찍어라
    x = -1
print (x)