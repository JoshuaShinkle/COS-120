def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    print("Exercise 7.10.12")
    for x in [2001, 2040, 1900, 2000]:
        print(isLeapYear(x))

main()