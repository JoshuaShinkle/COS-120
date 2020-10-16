def reverseWords(str):
    
    prevSpace = len(str)
    newString = ""

    for i in range(len(str)-1, -1, -1):
        if str[i] == " ":
            if prevSpace != i+1:
                newString = newString + str[i+1:prevSpace]
                newString = newString + " "
            prevSpace = i
    if prevSpace != 0:
        newString = newString + str[0:prevSpace]
    
    return newString

print(reverseWords("This is a test"))