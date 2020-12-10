import math
class Planet:
    def __init__(self, iname, iradius, imass, idistance): 
        self.name = iname
        self.radius = iradius
        self.mass = imass
        self.distance = idistance

    def getName(self):
        return self.name

    def getCircumference(self):
        return 2 * math.pi * self.radius

    def setName(self,newName):
        self.name=newName
        

p1=Planet("Z234",3000,2000,120000)
print(p1.name)
print(p1.getName())
p2=Planet("QQQ777",5000,8000,10000)
print(p2.name)
print(p2.getName())
p2.setName("Earth")
print(p2.getName())


class Sentence:
    def __init__(self,theSentence):
        self.sentence=theSentence

        

x=Sentence("Hello world")
print(x.sentence)
