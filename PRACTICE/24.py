class Volume:
    chapter = 1
    
    def __init__(self, paragraph): # paragraph은 volume.__dict__와 상관 없이 object가 생성될 때 만들어진다. 
        self.paragraph = paragraph
        Volume.chapter += 1
        
    def remove(self):
        del self.paragraph
        #pass
        
edition = Volume(1) # Volume.__dict__ = chapter, __init__, remove // edition.__dict__ = self.___가 들어있음
edition.paragraph = 10

edition.remove()
print(edition.__dict__)
print(Volume.__dict__)
