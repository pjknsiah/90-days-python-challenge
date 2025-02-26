def main():
    try:
        inpt = int(input("Enter a number: "))
        print(inpt)
    except ValueError:
        print("Invalid input, Enter an integer")

if __name__ == "__main__":
    main()