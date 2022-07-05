class Example: # 같은 페이지에 있을 경우 아웃풋은 __main__이 나옴. 
    def __str__(self):
        return __name__ # __name__ 변수에는 __main__ 값이 저장된다. 
    
thing = Example()
print(thing)




'''from Example import Example # from python_file_name import function_name, 즉 다른 파일의 함수를 갖다 씀 -> 이럴 경우 아웃풋은 Example이 나옴 
# class Example:
#     def __str__(self):
#         return __name__

a = Example()

print(a)

class Example:
    def __str__(self):
        return __name__'''
 