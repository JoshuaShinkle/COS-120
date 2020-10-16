
import calendar

def showASCII(string):
    for x in string:
        print(x + "=" + str(ord(x)))

print("L04-01")
showASCII("ABCD")
print()

def printASCIIRange(low,high):
    for x in range(low, high + 1):
        print(str(x) + "-" + chr(x))

print("L04-02")
printASCIIRange(65,69)
print()

def reverseString(string):
    for x in range(len(string)-1,-1,-1):
        print(string[x], end='')

print("L04-03")
reverseString("Hello")
print()

def reverseString(string):
    for x in range(-1, -len(string) - 1, -1):
        print(string[x], end='')

reverseString("Hello")
print()

def reverseString(string):
    print(string[::-1])
    
reverseString("Hello")
print()

def changeCase(char):
    if ord(char) > 96 and ord(char) < 123:
        return chr(ord(char) - 32)
    elif ord(char) < 91 and ord(char) > 64:
        return chr(ord(char) + 32)
    else:
        return char

print("L04-04")
print(changeCase("A"))
print()

def lowerCase(string):
    for x in string:
        if ord(x) < 91 and ord(x) > 64:
            print(changeCase(x), end='')
        else:
            print(x, end='')

print("L04-05")
lowerCase("123 HeLlo BOB #$% abcD")
print()
print()

def formatLongDate(date):
    print(str(calendar.month_name[int(date[:2])]) + " " + str(int(date[3:5])) + ", " + "20" + str(int(date[6:8])))
    

print("L04-06")
formatLongDate("09/05/99")
print()

def stringToASCIICodesString(string):
    for char in string:
        if ord(char) < 100:
            print("0" + str(ord(char)), end = '')

print("L04-07")
stringToASCIICodesString("BAD")
print()
print()

def ASCIICodesStringToString(string):
    i = 0
    j = 0
    for x in range(len(string)//3):
        print(chr(int(string[i:j+3])), end = '')
        i+=3
        j+=3
    
print("L04-08")
ASCIICodesStringToString("066065068")
print()
print()

def transposition2RailEncrypt(plainText): #2 rail trans. encryption
    evenChars = ""    
    oddChars = ""    
    for i in range (len(plainText)):
        if i % 2 == 0:                            
            evenChars = evenChars + plainText[i]
        else:            
            oddChars = oddChars + plainText[i]
    cipherText = oddChars + evenChars    
    return cipherText

def myEncrypt(string):
    for x in range(3):
        string = transposition2RailEncrypt(string)
    print(string)
    
    
print("L04-09")
myEncrypt("Hello Bob!")
