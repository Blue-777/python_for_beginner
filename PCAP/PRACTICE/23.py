class Control:
    my_ID = 1
    
    def say(self):
        return self.my_ID
    
class Button(Control):
    my_ID = 2
    
class Radio(Button):
    def say(self):
        return -self.my_ID
    
selection = Radio()
element = Control()
start = Button()

print(isinstance(selection, element))

# instance = object 
# class의 elements = variable, funciton