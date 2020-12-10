import re
#L09-01
def readWriteFile(file):
    inputFile = open(file, 'r')
    outputFile = open("rainfallfmt.txt", 'w')

    for line in inputFile:
        lst = line.split()
        outputFile.write("%+25s %5.1f\n" % (lst[0], float(lst[1])))

    inputFile.close()
    outputFile.close()

readWriteFile("rainfall.txt")

#L09-02
def writeTempConv():
    outputFile = open("tempconv.txt", 'w')

    outputFile.write("%+10s %+10s\n" % ("Fahrenheit", "Celsius"))
    
    for tempF in range(-300, 213):
        tempC = (tempF - 32) / 1.8
        outputFile.write("%10.3f %10.3f\n" % (tempF, tempC))
    
    outputFile.close()

writeTempConv()

#L09-03
def L08_03(file):
    inputFile = open(file, 'r')
    print(inputFile.readline())
    print(inputFile.readline())
    print(inputFile.readlines())
    inputFile.close()

print("L09-03")
L08_03("rainfall.txt")
#The list returned by readlines includes lines 3-25
print()

#L09-04
def L08_04(file):
    inputFile = open(file, 'r')
    print(inputFile.readlines())
    inputFile.close()

print("L09-04")
L08_04("rainfall.txt")
#This list returned by readlines includes all lines whereas in problem L09-03 it doesn't include lines 1 and 2
print()

#L09-05
def writeUpper(file):
    inputFile = open(file, 'r')
    outputFile = open("psalm112Upper.txt", 'w')

    allInFile = inputFile.read()
    outputFile.write(allInFile.upper())

    inputFile.close()
    outputFile.close()

writeUpper("Psalm112.txt")

#L09-06
def numDetails(file):
    inputFile = open(file, 'r')
    lineCount = 0
    wordCount = 0
    charCount = 0
    for line in inputFile:
        lineCount += 1
        words = line.split()
        for word in words:
            wordCount += 1
            charCount += len(word)
    
    print(lineCount)
    print(wordCount)
    print(charCount)
    
    inputFile.close()

print("L09-06")
numDetails("Psalm112.txt")
print()

#L09-07
def createConcord(file):
    inputFile = open(file, 'r')
    outputFile = open("concord.txt", 'w')

    d = {}
    lineNum = 1

    for line in inputFile:
        lines = line.split()
        for word in lines:
            word = word.lower()
            if word[-1].isalpha():
                if word in d:
                    if lineNum not in d[word]:
                        d[word].append(lineNum)
                else:
                    d[word] = [lineNum]
            else:
                word = word[:len(word)-1]
                if word in d:
                    if lineNum not in d[word]:
                        d[word].append(lineNum)
                else:
                    d[word] = [lineNum]
        lineNum += 1
    
    
    for key in d:
        outputFile.write("%+13s %-s\n" % (key, d[key]))

    inputFile.close()
    outputFile.close()

createConcord("forPirateConversion.txt")

#L09-08
def createSortedConcord(file):
    inputFile = open(file, 'r')
    outputFile = open("sortedconcord.txt", 'w')

    d = {}
    lineNum = 1

    for line in inputFile:
        lines = line.split()
        for word in lines:
            word = word.lower()
            if word[-1].isalpha():
                if word in d:
                    if lineNum not in d[word]:
                        d[word].append(lineNum)
                else:
                    d[word] = [lineNum]
            else:
                word = word[:len(word)-1]
                if word in d:
                    if lineNum not in d[word]:
                        d[word].append(lineNum)
                else:
                    d[word] = [lineNum]
        lineNum += 1
    
    
    for key in sorted(d):
        outputFile.write("%+13s %-s\n" % (key, d[key]))

    inputFile.close()
    outputFile.close()

createSortedConcord("forPirateConversion.txt")