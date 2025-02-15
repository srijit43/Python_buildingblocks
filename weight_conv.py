## Welcome to the weighing machine 

weight = float(input("Enter your weight: "))
unit = input("Is it Kilogram or pounds? (Kg or lbs)")

if unit == 'Kg':
    weight = weight * 2.205
    unit = 'lbs'

elif unit == 'lbs':
    weight = weight / 2.205
    unit = 'Kg'
    
else:
    print("Invalid unit. Please enter Kg or lbs")
    
print(f"Your weight is: {round(weight,1)} {unit}")
    
