def powerOf4(number):
    count = 0

    if number == ( number & (~(number -1))):
        while (number > 1):
            number >>= 1
            count = count + 1
        if count % 2 == 0:
            print("4^",count // 2)
            return True
        else:
            return False
number = int(input("enter your number :"))
if (powerOf4(number)):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')