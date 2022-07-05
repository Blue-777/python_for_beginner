f = open('foo.txt', 'w')
try: #try는 exception이나 finally 둘중 하나를 꼭 같이 써야함
    # 무언가를 수행한다.
    print(0/0)
finally: #try안에 에라가 있을때도 finallyh로 파일 닫아줌
    f.close()