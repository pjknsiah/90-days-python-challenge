def main():
    print("Hello, World!")
    while True:
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter a second number: "))
            break
        except ValueError:
            print("Invalid input")
    print(divide(a,b))

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