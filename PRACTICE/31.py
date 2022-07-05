class Un:
    value = "Ein"
    
    def __str__(self): 
        return "alice"
        
    def say(self):
        return self.value.lower() 
        
# class Deux(Un):
#     value = "Zwei"
    
# class Troi(Un):
#     def say(self):
#         return self.value.upper()
    
# class Quatre(Troi, Deux):
#     pass

# d = Quatre()
# b = Deux()

a =  Un()
print(a)

