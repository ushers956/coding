def reverseNumber(num):
    if(num > 0):

        last = num%10
        if(num//10>0):
            current_number = reverseNumber((int)(num // 10))
            return last*pow(10,len(str(current_number))) + current_number
        return num
    
n = int(input("enter your number : "))
print("reversed : ",reverseNumber(n))