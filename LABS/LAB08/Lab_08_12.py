import turtle

#Given
w=[83,99,2,3,1,7,54,1]
x=[23,12,67,5,4,11,2,84,12,16]
y={"staplers":2,"pencils":45,"erasers":12,"paper clips":200, "pens":84,"markers":12}
z={23012:2,77321:5,32332:234,77656:16,21321:802,99876:3}

#L08-01
def printList(list):
    for x in list:
        print(x)

print("L08-01")
printList(y)
print()

#L08-02
def printDict(dict):
    for x in dict:
        print (x, dict[x])

print("L08-02")
printDict(z)
print()

#L08-03
def printKeyDict(dict):
    for key, value in sorted(dict.items()):
        print(key, value)

print("L08-03")
printKeyDict(y)
print()

#L08-04
def printValueDict(dict):
    for key, value in sorted(dict.items(), key=lambda x: x[1]):
        print(key, value)

print("L08-04")
printValueDict(y)
print()

#L08-05
def addToList(list):
    value = int(input("Enter a value to add to list-> "))
    list.append(value)
    return list

print("L08-05")
print(addToList(x))
print()

#L08-06
def addToDict(dict):
    key = input("Enter key to add to dict-> ")
    value = int(input("Enter value to add to dict-> "))
    newPair = {key:value}
    dict.update(newPair)
    return dict

print("L08-06")
print(addToDict(y))
print()

#L08-07
def findDictValue(dict):
    key = input("What key are you searching?-> ")
    value = dict.get(key)
    if value == None:
        return "No such value"
    return value

print("L08-07")
print(findDictValue(y))
print()

#L08-08
def inList(list):
    value = int(input("Enter value you want to check-> "))
    for x in list:
        if x == value:
            return True
    return False

print("L08-08")
print(inList(x))
print()

#L08-09
def sortListAscend(list):
    sortedList = []
    copyList = []
    for x in list:
        copyList.append(x)
    for i in copyList:
        smallest = list[0]
        for j in list:
            if j < smallest:
                smallest = j
        sortedList.append(smallest)
        list.remove(smallest)
    return sortedList

print("L08-09")
print(sortListAscend(w))
print()

#L08-10
def mergeSortedLists(list1, list2):
    mergedLists = []
    compareIndex1 = 0
    compareIndex2 = 0
    i = 0
    while(1):
        if compareIndex1 == len(list1):
            for x in range(compareIndex2,len(list2)):
                mergedLists.append(list2[x])
            return mergedLists

        if compareIndex2 == len(list2):
            for x in range(compareIndex1,len(list1)):
                mergedLists.append(list1[x])
            return mergedLists

        if list1[compareIndex1] < list2[compareIndex2]:
            mergedLists.append(list1[compareIndex1])
            compareIndex1 += 1
        elif list2[compareIndex2] < list1[compareIndex1]:
            mergedLists.append(list2[compareIndex2])
            compareIndex2 += 1
        else:
            mergedLists.append(list1[compareIndex1])
            mergedLists.append(list2[compareIndex2])
            compareIndex1 += 1
            compareIndex2 += 1
        i += 1

print("L08-10")
w=[83,99,2,3,1,7,54,1]
x=[23,12,67,5,4,11,2,84,12,16]
a = sortListAscend(w)
b = sortListAscend(x)
print(mergeSortedLists(a,b))
print()

#L08-11
def easierSortedLists(list1, list2):
    mergedList = list1 + list2
    return sorted(mergedList)

print("L08-11")
w=[83,99,2,3,1,7,54,1]
x=[23,12,67,5,4,11,2,84,12,16]
a = sortListAscend(w)
b = sortListAscend(x)
print(easierSortedLists(a,b))
print()

#L08-12
def plotPoints(points):
    wn = turtle.Screen()
    lance = turtle.Turtle()
    lance.speed(0)

    xValues = []
    yValues = []
    for i in points:
        xValues.append(i[0])
    xMax = max(xValues)
    xMin = min(xValues)
    for j in points:
        yValues.append(j[1])
    yMax = max(yValues)
    yMin = min(yValues)
    wn.setworldcoordinates(xMin-10, yMin-10, xMax+10, yMax+10)

    lance.forward(xMax+9)
    lance.goto(0,0)
    lance.left(90)
    lance.forward(yMax+9)
    lance.right(90)

    for x in points:
        lance.up()
        lance.goto(x[0],x[1])
        lance.down()
        lance.begin_fill()
        lance.circle(0.2)
        lance.end_fill()
    lance.hideturtle()

points = [[39,2],[16,5],[14, 99],[2,1],[28,12],[12,28],[20,50],[38,77]]
plotPoints(points)

#L08-13
def switchKeyValue(dict):
    emptyDict = {}
    newDict = {}
    values = []
    for key, value in dict.items():
        if value in values:
            return emptyDict
        values.append(value)
        newDict.update({value:key})
    return newDict

print("L08-13")
print(switchKeyValue(y))
print()