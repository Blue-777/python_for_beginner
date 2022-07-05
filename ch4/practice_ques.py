#Q1 함수
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(2) +fib(1)  ## 재귀 호출: 함수 안에서 자기 자신을 부르는 거임 (n-2=0, n-1=0)

n = 2  => 1

fib(0) => 0

for i in range(10):   ##
    print(fib(i))  ##
    
#Q2 파일 읽고 쓰기 
'''f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0 
for line in lines:
    score = int(line)
    total += score #score
average = total/len(lines)

f = open("result.txt", "w")
f.write(str(average)) #?
f.close()'''
