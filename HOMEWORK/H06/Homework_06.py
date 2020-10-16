def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

def is_odd_modified(n):
    if is_even(n) == True:
        return False
    else:
        return True

def main():
    print()
    print("Exercise 7.10.7")
    userInt = int(input("Enter an Integer-> "))
    print(is_even(userInt))
    print()

    print("Exercise 7.10.8")
    userInt = int(input("Enter an Integer-> "))
    print(is_odd(userInt))
    print()

    print("Exercise 7.10.9")
    userInt = int(input("Enter an Integer-> "))
    print(is_odd_modified(userInt))
    print()

main()