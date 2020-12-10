import turtle
import random
import time

class Dice:
    def __init__(self,color,size,ulx,uly):
        self.color=color
        self.size=size
        self.upperLeftX=ulx
        self.upperLeftY=uly
        self.wn=turtle.Screen()
        self.t=turtle.Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(self.upperLeftX,self.upperLeftY)
        self.t.down()
        self.t.speed(0)
        self.value=0
        self.drawDie(0)

    def rollDie(self):
        roll = random.randint(1,6)
        self.drawDie(roll)

    def drawDie(self, roll):
        self.t.goto(self.upperLeftX,self.upperLeftY)
        self.t.clear()
        self.t.color("black", self.color)
        self.t.begin_fill()
        for x in range(4):
            self.t.forward(self.size)
            self.t.right(90)
        self.t.end_fill()

        if roll == 1:
            self.t.penup()
            self.t.goto(self.upperLeftX+self.size/2.5, self.upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("1" ,font=("Arial",self.size//2,"normal"))
        elif roll == 2:
            self.t.penup()
            self.t.goto(self.upperLeftX+self.size/2.5, self.upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("2" ,font=("Arial",self.size//2,"normal"))
        elif roll == 3:
            self.t.penup()
            self.t.goto(self.upperLeftX+self.size/2.5, self.upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("3" ,font=("Arial",self.size//2,"normal"))
        elif roll == 4:
            self.t.penup()
            self.t.goto(self.upperLeftX+self.size/2.5, self.upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("4" ,font=("Arial",self.size//2,"normal"))
        elif roll == 5:
            self.t.penup()
            self.t.goto(self.upperLeftX+self.size/2.5, self.upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("5" ,font=("Arial",self.size//2,"normal"))
        elif roll == 6:
            self.t.penup()
            self.t.goto(self.upperLeftX+self.size/2.5, self.upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("6" ,font=("Arial",self.size//2,"normal"))
    
class groupOfDice(Dice):
    def __init__(self,number,color,size,firstX,Y,xInterval):
        self.color=color
        self.size=size
        self.firstX = firstX
        self.Y = Y
        self.xInterval=xInterval
        self.wn=turtle.Screen()
        self.t=turtle.Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(firstX,Y)
        self.t.down()
        self.t.speed(0)
        self.group=[]
        self.number = number

    def drawDie(self, roll, x):
        upperLeftX = x
        upperLeftY = self.Y
        self.t.up()
        self.t.goto(upperLeftX,upperLeftY)
        self.t.down()
        self.t.color("black", self.color)
        self.t.begin_fill()
        for x in range(4):
            self.t.forward(self.size)
            self.t.right(90)
        self.t.end_fill()

        if roll == 1:
            self.t.penup()
            self.t.goto(upperLeftX+self.size/2.5, upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("1" ,font=("Arial",self.size//2,"normal"))
        elif roll == 2:
            self.t.penup()
            self.t.goto(upperLeftX+self.size/2.5, upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("2" ,font=("Arial",self.size//2,"normal"))
        elif roll == 3:
            self.t.penup()
            self.t.goto(upperLeftX+self.size/2.5, upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("3" ,font=("Arial",self.size//2,"normal"))
        elif roll == 4:
            self.t.penup()
            self.t.goto(upperLeftX+self.size/2.5, upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("4" ,font=("Arial",self.size//2,"normal"))
        elif roll == 5:
            self.t.penup()
            self.t.goto(upperLeftX+self.size/2.5, upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("5" ,font=("Arial",self.size//2,"normal"))
        elif roll == 6:
            self.t.penup()
            self.t.goto(upperLeftX+self.size/2.5, upperLeftY-self.size/1.25)
            self.t.pendown()
            self.t.write("6" ,font=("Arial",self.size//2,"normal")) 

    def rollGroup(self):
        x = self.firstX
        for i in range(1,self.number+1): 
            roll = random.randint(1,6)
            self.drawDie(roll, x)
            x += self.xInterval


def main():
    #Two dice, one white, one red, no group of dice
    die1=Dice("white",30,100,100)
    die2=Dice("red",30,200,200)
    for i in range(5):
        die1.rollDie()
        die2.rollDie()
        input("Press enter to roll again ")

    #2 groups of dice
    print("\n\n")
    attackDice=groupOfDice(3,"red",30,-60,280,50)
    defendDice=groupOfDice(3,"white",30,-60,240,50)
    for i in range(5):
        attackDice.rollGroup()
        defendDice.rollGroup()
        input("Press enter to roll again ")
        
main()
