# 부모/자식 상속 개념
class Cat:
    Species = 1 # 1는 false
    
    def get_species(self):
        return 'kitty'

class Tiger(Cat): # Cat:상속 하는 자. 따라서 Tiger는 Cat의 기능 및 변수를 사용할 수 있음. 
    # def get_species(self): # 상속받아서 같은게 있는 것을 overriding이라고 함. 만약 이것이 없을 경우 부모의 정의를 갖다 씀.
    #     return 'tiggy'
    
    def set_species(self):
        pass
creature = Tiger() # Tiger의 이름이 creature이고 이것은 class에서 나온 object임 -> 생명을 불어넣은 놈

# print(creature.get_species())
print(hasattr(creature, "Species"), hasattr(Cat, "set_species")) # hasattr는 갈호에 함수나 변수가 있는지 확인해서 true/false로 반환. 
# hasattr(class/object_이름, 해당 변수/함수_이름)

# class = ex)human, object = ex)alice // 기억하라!