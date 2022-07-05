try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else: #try에서 문제 없으면 else문 실행 
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

        