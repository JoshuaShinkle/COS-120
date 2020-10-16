import random

def showListFunctions(myClasses):
    print("a) ", end = '')
    print(myClasses[2:4])
    print()

    print("b-in) ", end = '')
    if 'COS 120' in myClasses:
        print("True")
    print("b-not in) ", end = '')
    if 'SYS 110' not in myClasses:
        print("False")
    print()

    print("c) ", end = '')
    print(myClasses + notMyClasses)
    print()
    
    print("d) ", end = '')
    print(myClasses[len(myClasses) - 1])
    print()

    print("e) ", end = '')
    print(len(myClasses))
    print()

    print("f) ", end = '')
    print(myClasses * 3)
    print()

    print("g) ", end = '')
    index = myClasses.index("ENG 110")
    print("ENG 110 found at index " + str(index))
    print()

print("L06-1")
myClasses = ["BIB 110", "COS 120", "ENG 110", "COS 103", "IAS 110"]
notMyClasses = ["COS 102", "SYS 120"]
showListFunctions(myClasses)
print()


def showTimeForClass(classes, times):
    selectedClass = input("Enter a course designation => ")
    index = myClasses.index(selectedClass)
    print(times[index])

print("L06-2")
times = [800, 900, 1100, 1400, 1400]
showTimeForClass(myClasses, times)
print()

def showTimeForClass2(combined):
    selectedClass = input("Enter a course designation => ")
    time = int(combined.index(selectedClass) + len(combined)/2)
    return combined[time]

print("L06-3")
combined = myClasses + times
print(showTimeForClass2(combined))
print()

def demoListMethods(aList):
    print("a) ", end = '')
    myClasses.append("SYS 120")
    print(myClasses)
    print()

    print("b) ", end = '')
    myClasses.insert(2, "SYS 120")
    print(myClasses)
    print()

    print("c) ", end = '')
    myClasses.pop(2)
    print(myClasses)
    myClasses.pop(len(myClasses)-1)
    print(myClasses)
    print()

    print("d) ", end = '')
    myClasses.sort()
    print(myClasses)
    print()

    print("e) ", end = '')
    myClasses.reverse()
    print(myClasses)
    print()

    print("f) ", end = '')
    index = myClasses.index("COS 120")
    print(index)
    print()

    print("g) ", end = '')
    count = myClasses.count("BIB 110")
    print(count)
    print()

    print("h) ", end = '')
    myClasses.remove("BIB 110")
    print(myClasses)
    print()

print("L06-4")
demoListMethods(myClasses)
print()

def reverseList(aList):
    newList = []
    for i in range(len(aList)-1, -1, -1):
        newList.append(aList[i])
    return newList

print("L06-5")
nums = [1,2,3,4,5]
print(reverseList(nums))

def reverseList2(aList):
    newList = []
    for x in aList:
        newList.append(x)
    newList.sort(reverse = True)
    return newList

print(reverseList2(nums))

def reverseList3(aList):
    newList = []

    for i in range(len(aList)-1, -1, -1):
        temp = [aList[i]]
        newList += temp
    return newList

print(reverseList3(nums))
print()

def shuffleToNewList(aList):
    newList = []
    for x in aList:
        newList.insert(random.randint(0, len(aList)), x)
    return newList

print("L06-6")
print(shuffleToNewList(nums))
print()

def shuffleInList(aList):
    for i in aList:
        index = aList.index(i)
        aList.pop(index)
        aList.insert(random.randint(0,len(aList)), i)
    return aList

print("L06-7")
print(shuffleInList(nums))