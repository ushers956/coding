def ReverseBits(number) :

    reversed = 0
    while (number > 0) :

        reversed = reversed << 1

        if(number & 1==1) :
            reversed = reversed ^ 1

        number = number >> 1