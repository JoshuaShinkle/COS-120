import random

manyLists=[[2,1,3,1,3,2],[3,4,5,6,7],[9,4,2,7,8,6,3,1,9],[12,3,2,1,2]]
moreLists = [[5,4,6],[2,1,3,9],[6,7,5,8,4]]
moreListsB = [[5,5,4,6,5,6], [6,7,5,8,4],[2,1,3,9,8]]

#L10-01
def commonLists(lst1,lst2):
    count = 0
    for i in lst1:
        for j in lst2:
            if i == j:
                count += 1
    return count

print("L10-01")
print(commonLists(manyLists, moreLists))
print()

#L10-02
def scrambleEachList(aListOfLists):
    for i in aListOfLists:
        random.shuffle(i)
    return aListOfLists

print("L10-02")
print(scrambleEachList(moreLists))
print()

#L10-03
def aListOfListsDupes(aListOfLists):
    newList = []
    for lst in range(len(aListOfLists)):
        newList.append([])
        for checkedElement in range(len(aListOfLists[lst])):
            for number in range(len(aListOfLists[lst])):
                if checkedElement < number and aListOfLists[lst][checkedElement] == aListOfLists[lst][number] and aListOfLists[lst][checkedElement] not in newList[lst]:
                    newList[lst].append(aListOfLists[lst][checkedElement])
                    break
    return newList

print("L10-03")
print(aListOfListsDupes(manyLists))
print()

#L10-04
def sumTheListPositions(ListOfLists1,ListOfLists2):
    newList = []
    for indexOfLst in range(len(ListOfLists1)):
        newList.append([])
        if len(ListOfLists1[indexOfLst]) > len(ListOfLists2[indexOfLst]):
            for index in range(len(ListOfLists1[indexOfLst])):
                if index < len(ListOfLists2[indexOfLst]):
                    newList[indexOfLst].append(ListOfLists1[indexOfLst][index] + ListOfLists2[indexOfLst][index])
                else:
                    newList[indexOfLst].append(ListOfLists1[indexOfLst][index])
        else:
            for index in range(len(ListOfLists2[indexOfLst])):
                if index < len(ListOfLists1[indexOfLst]):
                    newList[indexOfLst].append(ListOfLists1[indexOfLst][index] + ListOfLists2[indexOfLst][index])
                else:
                    newList[indexOfLst].append(ListOfLists2[indexOfLst][index])
    return newList

moreLists = [[5,4,6],[2,1,3,9],[6,7,5,8,4]]
print("L10-04")
print(sumTheListPositions(moreLists, moreLists))
print()

#L10-05
d1={"Bob":[5,4,3,2,1,2],"Sue":[2,3,1,4,4,3,2],"Jill":[6,5,6,4,3,1]}
d2={"Joe":[3,1,4,4],"Sally":[5,1,3,7],"Bob":[2,2,3,3,2]}
def sortCounts(aDictionary):
    for key in aDictionary.keys():
        aDictionary[key].sort()
    return aDictionary

print("L10-05")
print(sortCounts(d1))
print()

#L10-06
def lookupD(aDictionary):
    userInput = input("Enter a state or capitol => ")
    if userInput.lower() == "quit":
        return
    if userInput in aDictionary:
        return aDictionary[userInput]
    for key, value in aDictionary.items():
        if userInput == value:
            return key
    return "Not Found!"

print("L10-06")
print(lookupD({"Alaska":"Juneau","Idaho":"Boise","Ohio":"Columbus"}))
print()

#L10-07
classGrades={"COS120":{"Bob":[98,100,100,88],"Sue":[100,88,100,100],"Jill":[100,100,100,100]},"ENG110":{"Sue":[100,100,100,100,88],"Mary":[88,90,88,90,88],"John":[100,100,100,100,100],"Joe":[90,90,70,70,80]},"BIB231":{"Bob":[98,100,100,88],"Sue":[88,88,88,88],"Jill":[100,100,100,100]}}
def calcGrades(classD):
    for key1, value1 in classD.items():
        print("%s" % key1)
        for key2, value2 in value1.items():
            print("%+10s" % key2, end='')
            if sum(value2) / len(value2) >= 90:
                print("%+3s" % "A")
            elif sum(value2) / len(value2) >= 80:
                print("%+3s" % "B")
            elif sum(value2) / len(value2) >= 70:
                print("%+3s" % "C")
            elif sum(value2) / len(value2) >= 60:
                print("%+3s" % "D")
            else:
                print("%+3s" % "F")

print("L10-07")
calcGrades(classGrades)
print()

#L10-08
def convertD(classD):
    newDict = {}
    namesList = []
    
    for classes, namesDict in classD.items():
        for names, grades in namesDict.items():
            if names not in namesList:
                namesList.append(names)
                newDict[names] = 0

    for name in namesList:
        classGradDict = {}
        for classes, namesDict in classD.items():
            for names, grades in namesDict.items():
                if name == names:
                    classGradDict[classes] = classD[classes][names]
                    newDict[name] = classGradDict

    return newDict

print("L10-08")
print(convertD(classGrades))
print()