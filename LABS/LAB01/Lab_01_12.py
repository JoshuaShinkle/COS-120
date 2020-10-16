print("Lab Problem 01_01")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
print("Hello", firstName)
print("Hello " + firstName + "!")
print(firstName + " Hello!")
print(firstName, firstName, firstName, firstName)
print(firstName, lastName)
print(lastName + ", " + firstName)
print("")

print("Lab Problem 01_02")
earthWeight = int(input("Your Earth weight: "))
print("Your Moon weight:", earthWeight*.17)
print("Your Mercury weight:", earthWeight*.38)
print("Your Venus weight:", earthWeight*.91)
print("Your Saturn weight:", earthWeight*1.06)
print("Your Jupiter weight:", earthWeight*2.34)
print("")

print("Lab Problem 01_03")
moneyAvailable = float(input("How much money do you have available to gamble in Bitcoin: "))
bitcoinCost = float(input("What is Bitcoin’s current price in USD: "))
print("You could be the sorry owner of " + str(moneyAvailable/bitcoinCost) + " Bitcoins")
print("")

'''
First, I will output the problem number using a print statement.

Second, I will hard code the three entries using three arrays to save lines of code and make the
code more readable.

Third, I will calculate and assign each MPG of each entry to a different variable so I can use them in their
individual print statements and in calculating the total average. I will calculate the MPG by taking
index 0 and dividing it by index 1 of the same entry. The MPG for each is as following starting with
entry 1: 23.4, 24.0, and 20.0.

Fourth, I will output the MPG of each entry using print statements concatenated with the corresponding
MPG variable.

Finally, I will output the average MPG using a print statement concatenated with an expression that takes the
three MPG variables and calculates the average. The average is 22.46666666666667.
'''
print("Lab Problem 01_04")
entry1 = [234,10]
entry2 = [360,15]
entry3 = [200,10]
MPG1 = entry1[0]/entry1[1]
MPG2 = entry2[0]/entry2[1]
MPG3 = entry3[0]/entry3[1]
print("For entry 1 your MPG is " + str(MPG1))
print("For entry 2 your MPG is " + str(MPG2))
print("For entry 3 your MPG is " + str(MPG3))
print("Your average MPG for the three logbook entries is " + str((MPG1+MPG2+MPG3)/3))
print("")

'''
First, I will output the problem number using a print statement.

Second, I will prompt the user to input the total number of seconds they wish to convert.

Third, I will calculate the integers needed to convert from seconds to days, hours, and minutes. These three
integers will be the denominators in the conversions later on. These numbers are 86400, 3600, and 60 respectively.

Fourth, I will output the number of days using a print statement and floor division with the total seconds as the
numerator and the previously calculated denominator 86400.

Fifth, I will calculate and output the number of hours using a print statement and the remaining number of total
seconds after calculating the days. This remaining number of seconds can be found by using the modulus operator
with the original total of seconds and the previously calculated denominator 86400. The result of this will be the
new numerator that will be divided by a previously calculated demonimator to give me the number of hours.

Finally, I will repeat step five with new numbers to calculate and output the minutes and seconds.
'''
print("Lab Problem 01_05")
totalSeconds = int(input("Enter the total seconds you wish to convert to days, hours, minutes and seconds: "))
print("Days: " + str(totalSeconds//86400))
totalSeconds = totalSeconds%86400
print("Hours: " + str(totalSeconds//3600))
totalSeconds = totalSeconds%3600
print("Minutes: " + str(totalSeconds//60))
totalSeconds = totalSeconds%60
print("Seconds: " + str(totalSeconds))
print("")

#Runestone 2.13.1
'''
25
45
1.25
0.8
1
0
1
4
3
12
0
0
'''

#Runestone 2.13.2
'''
First, the parentheses are handled so the expression becomes 2 + 2 * 10 / 5 * 5

Second, the multiplication and division are handled starting from the left side and moving rightwards. The
expression then becomes 2 + 20 / 5 * 5 and then 2 + 4 * 5 and finally 2 + 20

Finally, the addition is handled and the expression is solved. The answer is 22.
'''

#Runestone 2.13.3
print("Runestone 2.13.3") 
currentTime = int(input("What is the current time(in hours)? "))
waitHours = int(input("How long do you want the clock to wait before the alarm goes off(in hours)? "))

print("When the alarm goes off the time will be: " + str((currentTime+waitHours)%24))
