def tailrec(n, num):

    if n > num:
        return
    print(n)

    tailrec(n + 1, num)

n = int(input("enter n to print to 10 to n:"))

tailrec(1, n)