def is_rightangled(a,b,c):
    x = a**2 + b**2
    c = c**2
    if abs(x-c) < 0.001:
        return True
    else:
        return False

def main():
    print("Exercise 7.10.10")
    a = float(input("Enter side a-> "))
    b = float(input("Enter side b-> "))
    c = float(input("Enter side c-> "))
    print(is_rightangled(a,b,c))

main()