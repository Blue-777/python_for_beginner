data = [261, 321]
try:
    print(data[-3]) # -3번째 리스트가 없음. 고로 에라 발생 
except Exception as exception: #에라시 실행
    print(exception.args) # output: ('list index out of range',) 나옴
else: #에라가 안 났을 경우 실행
    print("('success')")