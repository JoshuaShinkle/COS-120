def stripSpaces(myString):
    newString = ""
    for i in myString:
        if i != " ":
            newString = newString + i
    return newString

print(stripSpaces("I ran home very very quickly"))