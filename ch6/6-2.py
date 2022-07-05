#(6-2) 3과 5의 배수 합하기
'''result = []
i = 1
sum1 = 0
while i < 1000: 
    if i % 3 == 0:
        result.append(i)
        sum1 = sum1 + i
    elif i % 5 == 0:
        result.append(i)            
        sum1 = sum1 + i
    i = i + 1
print(result)
print(sum(result))
print(sum1)'''

# 문제: 예제)10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
#     1. 1000 미만의 자연수 구하기: 
#         result = [] 
#         while i < 1000:
#             i = i + 1
#     2. 필요한 변수 선언: i, sum
#         i = 1
#         sum1 = 0
#     3. if문으로 3의 배수와 5의 배수를 찾아내서 결과값에 담아라: 
#         if i % 3 == 0:
#             result.append(i)
#             sum1 = sum1 + i
#         elif i % 5 == 0:
#             result.append(i)            
#             sum1 = sum1 + i

'''result = []
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(0, 1000): 
    if i % 3 == 0: 
        sum1 += i
    elif i % 5 == 0:
        sum1 += i
    else:
        sum2 += i
#print(sum(i))
print('sum1 =',sum1)
print('sum2 =',sum2)
print('sum1 + sum2 =',sum1 + sum2)

for i in range(0, 1000):
    sum3 += i
print('sum3 =',sum3)'''