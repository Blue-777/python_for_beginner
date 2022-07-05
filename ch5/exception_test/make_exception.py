class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:    #try를 실행하면 exception 이 실행되는 순간 다음단계는 무시됨
    say_nick("바보")
    say_nick("천사")
except MyError as e:
    
    print(e)
