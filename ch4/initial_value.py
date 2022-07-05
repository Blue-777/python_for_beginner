def say_myself(name, old, man = True):
    print("my name is %s."%name)
    print("age is %d."%old)
    if man:
        print("man.")
    else:
        print("woman.")
        
say_myself("park", 27) #초기 값에서 입력 받아 True 값을 가진다 
say_myself("park", 27, True)
say_myself("park", 27, False)