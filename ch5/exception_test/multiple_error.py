'''try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError: #우리가 쓴 error message 
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")'''

'''try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e: #system에서 던져준 error message 
    print(e)
except IndexError as e:
    print(e)'''

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e: #먼저난 error만 표시됨. 괄호를 사용하여 함께 묶어 처리
    print(e)