def OnTime(n):
    iteration=0
    for i in range(1, n+1):
        iteration+=1
    print("when n is",n," iterations = ", iteration)

OnTime(10)
OnTime(20)
OnTime(42)

print("\nwith every 'n' the time taken and iteration will increase")