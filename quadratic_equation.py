#Write a python program to solve a quadratic equation
#ax^2 + bx + c = 0

import math

a = float(input("Enter first coefficient:"))
b = float(input("Enter first coefficient:"))
c = float(input("Enter first coefficient:"))

#Calculate the discriminant
x = b*2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if x > 0:
    
    
    # Two real and distinct roots
    root1 = (-b + math.sqrt(x)) / (2*a)
    root2 = (-b - math.sqrt(x)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif x == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(x)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")

