#Fibonacci sequence using recursion

def fibo(n):
    if n <= 1:
        return n 
    else:
        return (fibo(n-1) + fibo(n-2))
    
terms = int(input("Enter number of terms:"))
            
if terms<=0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Sequence:")
    for i in range(terms):
        print(fibo(i))

