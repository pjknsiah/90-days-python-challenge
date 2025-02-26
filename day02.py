import datetime

def main():
    name = input("Enter your name: ")
    try:
        age = int(input("How old are you: "))
    except ValueError:
        return"Invalid age input"
    currentYear = datetime.date.today().year
    birthYear = currentYear - age
    print(f"Hello, {name}. You were born in {birthYear} ")

if __name__ == "__main__":
    main()