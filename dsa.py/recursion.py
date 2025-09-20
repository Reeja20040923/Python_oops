def printNumbers(i,n):
    #base case
    if i>n:
        return
    #recursive case
    print(i,end=" ")
    printNumbers(i+1,n)
printNumbers(1,5)