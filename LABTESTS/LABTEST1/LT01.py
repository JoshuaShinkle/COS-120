print("Problem 1")
def straightLinesDistance(x1, y1, x2, y2):
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance

print(straightLinesDistance(12, 5, 3, -10))
print()

print("Problem 2")
def addStringsEncrypt(plainText, string2):
    if len(plainText) != len(string2):
        return plainText
    newString = ""
    for x in range(len(plainText)):
        newString += chr(ord(plainText[x])+ord(string2[x]))
    return newString
    
print(addStringsEncrypt("hello", "papers"))
print()

print("Problem 3")
def shipEstimate(numPallets, grossWeight, regionShippedTo):
    cost = 75
    if numPallets >= 1 and numPallets <= 5:
        cost += numPallets * 80
    elif numPallets >= 6 and numPallets <= 10:
        cost += numPallets * 65
    elif numPallets >= 11 and numPallets <= 20:
        cost += numPallets * 50
    elif numPallets > 20:
        cost += numPallets * 40

    if grossWeight >= 1001 and grossWeight <= 4000:
        cost += 200
    elif grossWeight >= 4001 and grossWeight <= 10000:
        cost += 400
    elif grossWeight > 10000 and grossWeight <= 30000:
        cost += 800
    elif grossWeight > 30000:
        print("Gross weight exceeded, cannot process charge!")
        return 0
    
    if regionShippedTo == 1:
        cost *= 1.1
    elif regionShippedTo == 2:
        cost *= 1.2
    elif regionShippedTo == 3:
        cost *= 1.3
    elif regionShippedTo == 4:
        cost *= 1.4
    elif regionShippedTo == 5:
        cost *= 1.5
    
    return cost

print(shipEstimate(45, 28000, 5))
print()

print("Problem 4")
def variableShiftEncrypt(plainText, digitalString):
    newString = ""
    newDigital = ""
    while(len(newDigital) < len(plainText)):
        newDigital += digitalString

    for i in range(len(plainText)):
        newString += chr(ord(plainText[i]) + int(newDigital[i]))
    return newString

print(variableShiftEncrypt("This is a test", "1135128792"))
print()

print("Problem 5")
def elongatedVowels(string):
    newString = ""
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            newString += i * 5
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            newString += i * 5
        else:
            newString += i
    return newString

print(elongatedVowels("WORKS WITH CAPITALS TOO"))
print()

print("Problem 6")
def theWordBeforeEverything(string):
    newString = ""
    lastWasChar = False
    for i in range(len(string)):
        if lastWasChar == False and string[i] != " ":
            newString += "The Word" + " "
            newString += string[i]
        else:
            newString += string[i]

        if i != len(string) - 1:
            if string[i] == " " and string[i+1] != " ":
                lastWasChar = False
            else:
                lastWasChar = True

    return newString

print(theWordBeforeEverything("You know its true!"))
print()