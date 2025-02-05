def main():
    inpt = int(input("Enter a number: "))
    print(factorial(inpt))

def factorial(number):
    if number < 0:
        return "Factorial not defined for negative numbers"
    elif number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)

main()