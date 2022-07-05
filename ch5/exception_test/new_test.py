try:
    4 / 0
except ZeroDivisionError as e: # e = error message // except은 어떤 에라를 무시하고 어떤 에라가 나는지 보여줌
    print(str(e) + ", 0 으로 나눌수 없다")