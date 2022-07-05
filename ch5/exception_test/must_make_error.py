class Bird:
    def fly(self):
        raise NotImplementedError 
        #NotImplementedError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly() #self를 쓰는 이유, 여기서 스스로를 불러와서 쓰니까 ㅎㅎ
