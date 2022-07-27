# 문제가 잘못됬음 
# 상속 받을 때 위아래는 상속이 안돼고 수평적 관계는 상속이 가능. 예) 할아버지와 아버지가 같이 상속 받는건 안돼고 형, 동생은 상속을 받릉 수 있음

class Diamond:
    pass

class Adamant(Diamond):
    pass

class Gem(Diamond):
    pass

class Jewel(Adamant, Diamond):
    pass

