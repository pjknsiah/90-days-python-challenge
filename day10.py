from math import sqrt

number = int(input("Enter a positive number: "))

try:
    sqroot = sqrt(number)
    print(f"The square root of {number} is {sqroot:.4f}")
except ValueError:
    print("Invalid input. Enter a positive number")