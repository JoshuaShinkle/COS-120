def printChars1(word):
    for x in range(0, len(word)):
        print(word[x])

print("L05-1")
printChars1("right")
print()

def printChars2(word):
    for x in word:
        print(x)

print("L05-2")
printChars2("right")
print()

def printChars3(word):
    buildWord = ""
    for x in word:
        buildWord = buildWord + x
        print(buildWord)

print("L05-3")
printChars3("right")
print()

def printChars4(word):
    for j in range(0,len(word)):
        print(word[:j+1])

print("L05-4")
printChars4("right")
print()

def printInReverse1(inString):
    buildWord = ""

    for x in inString:
        placeHolder = buildWord
        buildWord = ""
        buildWord = x
        buildWord = buildWord + placeHolder
        print(buildWord)

print("L05-5")
printInReverse1("hello")
print()

def printInReverse2(inString):
    for i in range(-1, -len(inString)-1, -1):
        print(inString[-1:i-1:-1])

print("L05-6")
printInReverse2("hello")
print()

def length(inString):
    count = 0
    for x in inString:
        count += 1
    return count

print("L05-7")
print(length("1234"))
print()

def sliceStr(inString, From, To):
    sliced = ""
    for i in range(From, To):
        sliced = sliced + inString[i]
    return sliced

print("L05-8")
print(sliceStr("A new start",2,5))
print()

def inString(thisString, targetString):
    for i in range(len(targetString)):
        if targetString[i] == thisString[0]:
            count = 0
            for j in range(1, len(thisString)):
                if i+j == len(targetString):
                    return False
                if targetString[i+j] != thisString[0+j]:
                    break
                count += 1
            if count == len(thisString) - 1:
                return True 
    return False

print("L05-9")
print(inString("all", "all or none at all"))
print()

def concatenate(firstString, secondString):
    baseString = "ab"
    firstReplace = baseString.replace("a", firstString)
    secondReplace = firstReplace.replace("b", secondString)
    return secondReplace

print("L05-10")
print(concatenate("Hello123", "1234"))
print()

def find(thisString, inString):
    for i in range(len(inString)):
        if inString[i] == thisString[0]:
            count = 0
            for j in range(1, len(thisString)):
                if i+j == len(inString):
                    return False
                if inString[i+j] != thisString[0+j]:
                    break
                count += 1
            if count == len(thisString) - 1:
                return i 
    return -1

print("L05-11")
print(find("all", "not at all"))
print()

def replace(inString,findString,rplString):
    newString = inString
    for i in range(len(newString)-1):
        if newString[0+i:len(findString)+i] == findString:
            newString = newString[0:i] + rplString + newString[i+len(findString):]
    return newString

print("L05-12")
print(replace("I ran ran ran home!", "ran", "walked"))
print()