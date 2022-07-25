# 추상 메서드: abstract method

class SuperClass:
    def method(self):
        pass
    
class SubClass1(SuperClass):
    def method(self):
        print('overriding method() from SubClass1')

class SubClass2(SuperClass):
    pass

# main code part
sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()