#swap 2 nums. Use a temp

a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

print(f"Original values: {a} and {b}")

temp = a
a = b
b = temp

print(f"Swapped values: {a} and {b}")