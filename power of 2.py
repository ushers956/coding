def power2(number):

 if (number == 0):
    return 0
 if ((number & (~(number - 1))) == number):
   return 1
 return 0

number = int(input("enter the number : "))

if(power2(number)):
  print("\nthe number is power of 2")
else:
  print("\nthe number is not power of 2")