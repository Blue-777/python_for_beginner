try:
    f = open("나없는파일", 'r')
except FileNotFoundError: #프로그래밍을 하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다. 오류를 그냥 회피
    pass