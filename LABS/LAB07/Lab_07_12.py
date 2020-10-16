import turtle
import random

print("L07-1")
def averageASCII(string):
    sum = 0
    avg = 0
    for x in string:
        sum += ord(x)
    avg = sum / len(string)
    return avg

print(averageASCII("ABC"))

print("L07-2")
def merge(string1, string2):
    newString = ""
    for x in range(len(string1)):
        newString += string1[x]
        newString += string2[x]
    return newString

print(merge("abcd", "ABCD"))

print("L07-3")
def countUpperCaseLetters(string):
    numUpper = 0
    for x in string:
        if ord(x) <= ord("Z") and ord(x) >= ord("A"):
            numUpper += 1
    return numUpper

print(countUpperCaseLetters("This IS a very sTraNge sentence."))

print("L07-4")
def countUpperCaseWords(string):
    numUpperWords = 0
    check = True
    for i in range(len(string)):
        if check == True:
            if ord(string[i]) <= ord("Z") and ord(string[i]) >= ord("A"):
                numUpperWords += 1
                check = False
        if string[i] == " ":
            check = True
    return numUpperWords

print(countUpperCaseWords("This IS a very sTraNge sentence."))

print("L07-5")
def howManyOccurrences(string1, string2):
    numOccur = 0
    for i in range(len(string2)):
        if string1 == string2[i:i+len(string1)]:
            numOccur += 1
    return numOccur

print(howManyOccurrences("dd", "a b c d dddd e fgddd"))

print("L07-6")
def invertedWords(sentence):
    newSentence = ""
    count = 0
    first = True
    grabbed = False
    placeHolder = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            newSentence += sentence[i-1:i-count-1:-1]
            if grabbed == True:
                newSentence += sentence[placeHolder]
                grabbed = False
            newSentence += " "
            count = 0
        elif i == len(sentence)-1:
            newSentence += sentence[i:i-count-1:-1]
        else:
            if first == True:
                placeHolder = i
                first = False
                grabbed = True
            else:
                count += 1
    return newSentence

print(invertedWords("This is a test"))

print("L07-7")
def lookup(word):
    keyedString = "cow-a domesticated mammal;kiwi-a fruit from New Zealand;hat-an article of clothing worn on the head"
    index = keyedString.find(word + "-")
    if index == -1:
        return word + " NOT FOUND IN KEYED STRING"
    newString = keyedString[index:]
    endOfDef = newString.find(";")
    if endOfDef == -1:
        return newString[len(word)+1:]
    return newString[len(word)+1:endOfDef]

word = input("Enter the word to lookup: ")
print(lookup(word))

print("L07-8")
def centerOutTranspose(plaintext):
    newString = ""
    txt = plaintext
    for x in plaintext:
        index = len(txt) // 2
        newString += txt[index]
        txt = txt[:index] + txt[index+1:]
    return newString

print(centerOutTranspose("ABCDEFG"))

print("L07-9")
def turtleOut():
    turtle.setworldcoordinates(-1, -1, 201, 201)
    t = turtle.Turtle()
    t.up()
    t.goto(20,20)
    t.down()
    for x in range(4):
        t.forward(160)
        t.left(90)
    t.up()
    t.goto(random.randint(21,179), random.randint(21,179))
    x,y = t.position()
    while((x>20 and x<180) and (y>20 and y<180)):
        t.goto(random.randint(21,179), random.randint(21,179))
        t.forward(random.randint(10,20))
        lorR = random.randint(1,2)
        if lorR == 1:
            t.left(random.randint(0,360))
        else:
            t.right(random.randint(0,360))
        x,y = t.position()

turtleOut()
