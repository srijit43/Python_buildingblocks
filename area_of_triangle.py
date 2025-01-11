#Python program to find area of a triangle. 
#Area of a triangle is given by the formula 0.5 * base * height
#This will take input from the end user

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

if base > 0.0 and height > 0.0:
    area = 0.5 * base * height
    print("Area of the triangle is:", area)
else:
    print("Please enter positive values for base and height.")