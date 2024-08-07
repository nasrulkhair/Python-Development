# Parent Class and Child Class

#Creating parent class

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):  #kena define the variable yang letak dalam bracket
        #assigning what is nam
        self.name = nam
        print(self.name,"constructed")
        
    #2nd definition class
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        
#Creating a child class
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
        
# calling the classes
s = PartyAnimal("Nasrul")
s.party()

j = FootballFan("khair")
j.party()
j.touchdown()