def printNumbers(i,n):
    #base case
    if i>n:
        return
    #recursive case
    print(i,end=" ")
    printNumbers(i+1,n)
printNumbers(1,5)

#factorial using recursion
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

print(fact(5))

#Recursive stack
def fun(n):
    if (n==0):
        return
    fun(n-1)
    print(n,end = " ")

fun(3)

# Recursive Tree example
# Fibonacci
class Solution :
    def fib(self,n: int) ->int:
        #base case
        if(n==0 or n==1):
            return n
        #recursive case
        return self.fib(n-1)+self.fib(n-2)

# Power of 2 
def isPowerOfTwo(self ,n:int) -> bool:
    while n%2==0:
        n//=2

    return n==1   


#GCD
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(15,50))

# LCM
def lcm(a,b):
    return a*b//gcd(a,b)
print(lcm(15,50))

# find power(x,n)
def findpow(x,n):
    if n==0:
        return 1
    a = findPow(x,n//2)
    if n%2==0:
        return a*a
    else :
        return a*a*x