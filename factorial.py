# program to find factorial of any number using recursion
def fac(n):
    # when n is 1 or 0, return 1
    if(n==1 or n==0):
        return 1
    #factorial of n = n*n-1*n-2...1
    return n*fac(n-1)
n = int(input("enter your number :"))
print ("factorial of", n,"is :",fac(n))
print("the time complexity of recursive functions are O(nlogn)")