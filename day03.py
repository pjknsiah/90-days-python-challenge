def main():
    try:
        age = int(input("Enter your age: "))
        print("You are eligible to vote" if age >= 18 else "You are too young to vote")
    except ValueError:
        return "Invalid age input"

if __name__ == "__main__":
    main()