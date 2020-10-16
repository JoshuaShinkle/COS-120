import random
import math

print("Exercise 5.7.16")
for x in range(10):
    num = random.random()
    print(num)
print("")

print("Exercise 5.7.17")
for x in range(10):
    num = random.randrange(25,36)
    print(num)
print("")

print("Exercise 5.7.18")
hypotenuse = math.hypot(3,4)
print(hypotenuse)
print("")

print("Exercise 5.7.19")
pi = 0
denom = 1
for x in range(10000000):
    pi = pi + (1/denom - 1/(denom+2))
    denom = denom + 4
print("My approximated pi =", pi*4)
print("Math.pi =", math.pi)
