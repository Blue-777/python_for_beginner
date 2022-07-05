class HousePark:
    lastname = "박"
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s,%s여행을 가다."%(self.fullname, where))

pey = HousePark()
pes = HousePark()

pey.fullname = pey.lastname + name

pey.setname("응용")
print(pey.fullname)
