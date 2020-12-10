import random

def genRandIntsEndWith11():
    numList = []
    num = 0
    while num != 11:
        num = random.randint(0,11)
        numList.append(num)

    return numList

print(genRandIntsEndWith11())

def getIntegers():
    lst = []
    while(1):
        num = input("Enter an integer-> ")
        if num.lower() == 'quit':
            break
        lst.append(int(num))
    return lst

print(getIntegers())