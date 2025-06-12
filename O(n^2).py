def ONsquaretime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            iteration+=1
        print("")
    print("\nwhen n is",n," iterations = ",iteration,"\n")

ONsquaretime(5)
ONsquaretime(4)
ONsquaretime(3)

print("\nwith every 'n' the time taken equals n^2")
print("0(n^2)")