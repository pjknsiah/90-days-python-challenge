def main():
    try:
        inpt = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, Enter an integer")

if __name__ == "__main__":
    main()