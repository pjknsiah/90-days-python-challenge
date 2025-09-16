import re

def main():
    test_email = input("Enter email to validate: ")
    if validate_email_basic(test_email):
        print("Valid email!")
    else:
        print("Invalid email!")

def validate_email_basic(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    main()