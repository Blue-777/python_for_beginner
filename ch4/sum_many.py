#입력값을 모두 더하는 함수 
'''def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i #*args에 입력받음 모든 값을 더한다
    return sum 

result = sum_many(1, 2, 3)
print(result)

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)'''

def sum_mul(choice, *args):
    if choice == "sum": #입력 인수 choice에 'sum' 을 입력받았을 때 
        result =0
        for i in args:
            result = result + i #*args에 입력받음 모든 값을 더한다
    elif choice == "mul": #입력 인수 choice에 'mul' 을 입력받았을 때 
        result =1
        for i in args:
            result = result * i #args에 입력받음 모든 값을 곱한다
    return result 

result = sum_mul('sum', 1,2,3,4,5)
print(result)

result = sum_mul('mul', 1,2,3,4,5)
print(result)