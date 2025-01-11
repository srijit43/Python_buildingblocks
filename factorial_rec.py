#Factorial of a number using recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
number = int(input("Enter a number to find factorial:"))

if number==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of",number,"is",factorial(number))
