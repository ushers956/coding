from math import sqrt
number = int(input(" enter your number :"))
print("\n")

if number > 1:


    for i in range(2, int(sqrt(number))+1):


        if (number % i) == 0:
            print(number, "is not a prime number")
            break

        else:
            print(number, "is a prime number")


else:
    print(number, "is not a prime number")