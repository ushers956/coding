def print_factors(number):
    print("the factors of",number,"are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


number = int(input("enter your numbers to find it's factors:"))

print_factors(number)