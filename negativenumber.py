def xyz(n):
    n = int(input("enter a number:"))
    if n > 0:
        print("positive number")
        xyz(n)
    elif n == 0:
        print("zero")
        xyz(n)

    else:
        print("negitive number")

xyz(9)