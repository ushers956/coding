numberlargest = int(input("enter largest number : "))
numbersmallest = int(input("enter smallest number : "))

while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore


print("HCF is :",numberlargest)