print("L02-0")
for i in range(10,21):
    print(i)
print()

print("L02-1")
for i in range(0,6):
    print(i)
print()

print("L02-2")
for i in range(1,6):
    print(i)
print()

print("L02-3")
for i in range(1,101):
    print(i)
print()

print("L02-4")
for i in range(100,0,-1):
    print(i)
print()

print("L02-5")
for i in range(3,34,3):
    print(i)
print()

print("L02-6")
for i in range(33,2,-3):
    print(i)
print()

print("L02-7")
sumNum = 0
for i in range(1,11):
    sumNum += i
print(sumNum)
print()

print("L02-8")
prodNum = 1
for i in range(1,11):
    prodNum *= i
print(prodNum)
print()

print("L02-9")
names = ["Mary","Joe", "Adam"]
for i in names:
    for j in range(1,4):
        print(j, i)
print()

print("L02-10")
startNum = int(input("Enter starting number: "))
endNum = int(input("Enter ending number: "))
for i in names:
    for j in range(startNum,endNum+1):
        print(j, i)
print()

print("L02-11")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()
print()

print("L02-12")
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()
print()

print("L02-13")
for i in range(1,4):
    for j in range(1,4):
        print(str(i)+"x"+str(j)+"="+str(i*j))
print()

print("L02-14")
startNum = int(input("Enter starting number: "))
endNum = int(input("Enter ending number: "))
for i in range(startNum,endNum+1):
    for j in range(startNum,endNum+1):
        print(str(i)+"x"+str(j)+"="+str(i*j))
