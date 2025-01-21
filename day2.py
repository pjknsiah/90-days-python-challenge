def main():
    name = input("Enter your name: ")
    try:
        age = int(input("How old are you: "))
    except ValueError:
        return"Invalid age input"
    print(f"Hello, {name}. You were born in ")

if __name__ == "__main__":
    main()