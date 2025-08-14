def ways(stairs):

    if stairs<0:
        return 0
    
    if stairs==0:
        return 1
    twoSteps = 0
    oneStep=0


    if(stairs>=2):
        twoSteps = ways(stairs-2)

    oneStep = ways(stairs-1)

    return twoSteps + oneStep

stairs = int(input("enter number of steps : "))

print("number two ways to climb : ",ways(stairs))