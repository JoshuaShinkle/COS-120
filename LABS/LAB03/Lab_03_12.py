print("L03-01")
'''
The IDLE environment will print 4.
Then it will print 4 on a new line.
Then it will print 20 on a new line.
'''

from math import *
def demoCalls():
    sqrt(16)
    print(sqrt(16))
    x=sqrt(16)
    print(x)
    y=sqrt(16) * sqrt(25)
    print(y)

demoCalls()
print()

'''
I got what I expected for the most part.
Although I predicted the numbers correctly,
they were printed as floats instead of the
integers I predicted.
'''

##def mySQRT(n,iters):
##    X=1
##    for i in range(iters):
##        X=1/2*(X+n/X)
##
##def testmySQRT():
##    mySQRT(16,100)
##    print(mySQRT(16,100))
##    x= mySQRT(16,100)
##    print(x)
##    y= mySQRT(16,100) * mySQRT (25,100)
##    print(y)
##
##testmySQRT()

'''
You should theoretically get the same thing as before.
However, you get different results because testmySQRT()
calls mySQRT() in its body to do some calculations and
mySQRT() doesn't return a number. Because it doesn't return
a number, no calculations can be done and therefore it prints
"none" and "none" when testmySQRT() is run. The error message
means you can't multiply two nonexistant things or "None" together.
'''

##def mySQRT(n,iters):
##    X=1
##    for i in range(iters):
##        X=1/2*(X+n/X)
##    print(X)
##
##def testmySQRT():
##    mySQRT(16,100)
##    print(mySQRT(16,100))
##    x= mySQRT(16,100)
##    print(x)
##    y= mySQRT(16,100) * mySQRT (25,100)
##    print(y)
##
##testmySQRT()

'''
It's better to return the value from the function that way it
can be used in another function or be assigned to a variable.
If it prints instead of returning, then when testmySQRT() calls
it to print, it prints "None" and executes the print in mySQRT()
which makes for a confusing output in the IDLE environment.
Returning also provides the more useful abstraction.
'''

def mySQRT(n,iters):
    X=1
    for i in range(iters):
        X=1/2*(X+n/X)
    return X

def testmySQRT():
    mySQRT(16,100)
    print(mySQRT(16,100))
    x= mySQRT(16,100)
    print(x)
    y= mySQRT(16,100) * mySQRT (25,100)
    print(y)

testmySQRT()
print()

print("L03-02")
for x in range(3):
    print("in the loop")
print()

for x in range(3,0,-1):
    print("in the loop")
print()

for x in ("Josh", "Lance", "Logan"):
    print("in the loop")
print()

for x in range(0,6,2):
    print("in the loop")
print()

for x in [100,324,56]:
    print("in the loop")
print()

for x in range(12,3,-3):
    print("in the loop")
print()

print("L03-03")
def schoolDaze(n):
    if (n<1):
        print("That age is too young for schooling.")
    if (n>18):
        print("That age is beyond high school.")
    if (n>=1) and (n<=3):
        print("That age is in Nursery.")
    if (n>=4) and (n<=5):
        print("That age is in Preschool.")
    if (n>=6) and (n<=11):
        print("That age is in Elementary.")
    if (n>=12) and (n<=13):
        print("That age is in Middle School.")
    if (n>=14) and (n>=18):
        print("That age is in High School.")

age = int(input("Enter age-> "))
schoolDaze(age)
print()

print("L03-04")
def schoolDaze(n):
    if (n<1):
        print("That age is too young for schooling.")
    else:
        if (n>18):
            print("That age is beyond high school.")
        else:
            if (n>=1) and (n<=3):
                print("That age is in Nursery.")
            else:
                if (n>=4) and (n<=5):
                    print("That age is in Preschool.")
                else:
                    if (n>=6) and (n<=11):
                        print("That age is in Elementary.")
                    else:
                        if (n>=12) and (n<=13):
                            print("That age is in Middle School.")
                        else:
                            print("That age is in High School.")

age = int(input("Enter age-> "))
schoolDaze(age)
print()

print("L03-05")
def schoolDaze(n):
    if (n<1):
        print("That age is too young for schooling.")
    elif (n>18):
        print("That age is beyond high school.")
    elif (n>=1) and (n<=3):
        print("That age is in Nursery.")
    elif (n>=4) and (n<=5):
        print("That age is in Preschool.")
    elif (n>=6) and (n<=11):
        print("That age is in Elementary.")
    elif (n>=12) and (n<=13):
        print("That age is in Middle School.")
    else:
        print("That age is in High School.")

age = int(input("Enter age-> "))
schoolDaze(age)
print()
'''
The user of the function will not see any difference.
'''

print("L03-06")
def PRS(p1,p2):
    if p1 == "paper" and p2 == "rock":
        print("paper covers rock")
    elif p1 == "paper" and p2 == "scissors":
        print("scissors cuts paper")
    elif p1 == "paper" and p2 == "paper":
        print("tie")
    elif p1 == "rock" and p2 == "paper":
        print("paper covers rock")
    elif p1 == "rock" and p2 == "scissors":
        print("rock dulls scissors")
    elif p1 == "rock" and p2 == "rock":
        print("tie")
    elif p1 == "scissors" and p2 == "paper":
        print("scissors cuts paper")
    elif p1 == "scissors" and p2 == "rock":
        print("rock dulls scissors")
    elif p1 == "scissors" and p2 == "scissors":
        print("tie")
    else:
        print("Invalid moves!")

p1 = input("What's your move: ").lower()
p2 = input("What's your move: ").lower()

PRS(p1,p2)
print()

print("L03-07")
def testPRS():
    PRS("paper","paper")
    PRS("paper","rock")
    PRS("paper","scissors")
    PRS("rock","paper")
    PRS("rock","rock")
    PRS("rock","scissors")
    PRS("scissors","paper")
    PRS("scissors","rock")
    PRS("scissors","scissors")

testPRS()
print()

print("L03-08")
def calcAutoPremium(age,numDoors,gender):
    if age<21:
        if numDoors==2:
            print ("High Risk")
            premium = 2500
            if gender == "male":
                premium = premium*2
            elif gender == "female":
                premium = premium*(2/3)
        else:
            print ("Semi-High Risk")
            premium=1900
            if gender == "male":
                premium = premium*2
            elif gender == "female":
                premium = premium*(2/3)
    else:
        if numDoors==2:
            print ("Medium Risk")
            premium=1500
        else:
            print ("Low Risk")
            premium=800
    monthlyPayment=premium/12.0
    return monthlyPayment

monthlyPayment = calcAutoPremium(18,2,"male")
print()

print("L03-09")
def testAutoPremium():
    for i in("male","female"):
        for j in[2,4]:
            for n in[18,21,30]:
                print(calcAutoPremium(n,j,i))
            
testAutoPremium()
print(monthlyPayment)
