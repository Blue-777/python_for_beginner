class Content:
    title = "None"

    def __init__(self, this):
        self.name = this + "than" + Content.title  # self.name 클래스 전역 글러벌변수,  Content.name  (클래스명 인스턴스명으로도 쓸수) 
        print(self.name)
        

 #   def __str__(self)

#class end 


text_1 = Content("Paper") # text_1 인스턴스(객체,오프젝트) 만들떄 __init__ 함수의  this  "Paper" 넣음 text_1.name
text_2 = Content("Article") # text_2 인스턴스 만들고

print(text_1.title)
print(text_2.name)


# #text_3 = Content("Alice","park","동은")
print(text_1.title == text_2.name)

