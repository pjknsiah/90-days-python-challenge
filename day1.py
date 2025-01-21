def main():
    print("Hello, World!")
    while True:
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter a second number: "))
            break
        except ValueError:
            print("Invalid input. Enter a valid integer")
    print("Select an operation\n1. Add\n2. Multiply\n3. Subtract\n4. Divide")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in [1, 2, 3, 4]:
                break
        except ValueError:
            print("Invalid input. Enter a valid integer between 1 and 4")
    if choice == 1:
        result = add(a, b)
    elif choice == 2:
        result = multiply(a, b)
    elif choice == 3:    
        result = subtract(a, b)
    else:
        result = divide(a, b)
    print(f"The result of the operation is {result}")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return~"Denominator must be non-zero"

if __name__ == "__main__":
    main()