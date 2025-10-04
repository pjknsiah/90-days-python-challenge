import re
import sys
from typing import List, Tuple

class EmailValidator:
    """Email validation using regular expressions"""
    
    def __init__(self):
        # Basic email pattern - we'll build this step by step
        self.basic_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # More comprehensive pattern
        self.advanced_pattern = r'^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,253}\.[a-zA-Z]{2,}$'
        
        # Compiled patterns for better performance
        self.basic_regex = re.compile(self.basic_pattern)
        self.advanced_regex = re.compile(self.advanced_pattern)
    
    def validate_basic(self, email: str) -> bool:
        """
        Basic email validation using simple regex
        
        Args:
            email (str): Email address to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        return bool(self.basic_regex.match(email))
    
    def validate_advanced(self, email: str) -> Tuple[bool, str]:
        """
        Advanced email validation with detailed feedback
        
        Args:
            email (str): Email address to validate
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        # Check if email is empty or None
        if not email:
            return False, "Email cannot be empty"
        
        # Check length constraints
        if len(email) > 254:
            return False, "Email too long (max 254 characters)"
        
        # Check for @ symbol
        if email.count('@') != 1:
            return False, "Email must contain exactly one @ symbol"
        
        # Split email into local and domain parts
        try:
            local, domain = email.split('@')
        except ValueError:
            return False, "Invalid email format"
        
        # Validate local part (before @)
        if not self._validate_local_part(local):
            return False, "Invalid local part (before @)"
        
        # Validate domain part (after @)
        if not self._validate_domain_part(domain):
            return False, "Invalid domain part (after @)"
        
        # Final regex check
        if not self.advanced_regex.match(email):
            return False, "Email format is invalid"
        
        return True, "Valid email address"
    
    def _validate_local_part(self, local: str) -> bool:
        """Validate the local part of email (before @)"""
        if not local or len(local) > 64:
            return False
        
        # Local part pattern
        local_pattern = r'^[a-zA-Z0-9._%+-]+$'
        
        # Cannot start or end with a dot
        if local.startswith('.') or local.endswith('.'):
            return False
        
        # Cannot have consecutive dots
        if '..' in local:
            return False
        
        return bool(re.match(local_pattern, local))
    
    def _validate_domain_part(self, domain: str) -> bool:
        """Validate the domain part of email (after @)"""
        if not domain or len(domain) > 253:
            return False
        
        # Domain must have at least one dot
        if '.' not in domain:
            return False
        
        # Split domain into parts
        parts = domain.split('.')
        
        # Each part must be valid
        for part in parts:
            if not part:  # Empty part (consecutive dots)
                return False
            if len(part) > 63:  # Each label max 63 chars
                return False
            if not re.match(r'^[a-zA-Z0-9-]+$', part):
                return False
            if part.startswith('-') or part.endswith('-'):
                return False
        
        # TLD (last part) must be at least 2 characters and only letters
        if len(parts[-1]) < 2 or not re.match(r'^[a-zA-Z]+$', parts[-1]):
            return False
        
        return True
    
    def demonstrate_regex_patterns(self):
        """Demonstrate basic regex patterns used in email validation"""
        
        print("=== REGEX PATTERN DEMONSTRATIONS ===\n")
        
        # \d - digits
        digit_pattern = r'\d+'
        test_string = "There are 123 apples and 456 oranges"
        matches = re.findall(digit_pattern, test_string)
        print(f"\\d pattern: {digit_pattern}")
        print(f"Test string: '{test_string}'")
        print(f"Matches: {matches}\n")
        
        # \w - word characters
        word_pattern = r'\w+'
        test_string = "hello_world123 and special-chars!"
        matches = re.findall(word_pattern, test_string)
        print(f"\\w pattern: {word_pattern}")
        print(f"Test string: '{test_string}'")
        print(f"Matches: {matches}\n")
        
        # \s - whitespace
        space_pattern = r'\s+'
        test_string = "word1   word2\tword3\nword4"
        matches = re.findall(space_pattern, test_string)
        print(f"\\s pattern: {space_pattern}")
        print(f"Test string: '{repr(test_string)}'")
        print(f"Matches: {[repr(m) for m in matches]}\n")
        
        # + - one or more
        plus_pattern = r'a+'
        test_string = "a aa aaa banana"
        matches = re.findall(plus_pattern, test_string)
        print(f"+ pattern: {plus_pattern}")
        print(f"Test string: '{test_string}'")
        print(f"Matches: {matches}\n")
        
        # * - zero or more
        star_pattern = r'ab*c'
        test_string = "ac abc abbc abbbc axc"
        matches = re.findall(star_pattern, test_string)
        print(f"* pattern: {star_pattern}")
        print(f"Test string: '{test_string}'")
        print(f"Matches: {matches}\n")
        
        # ? - zero or one
        question_pattern = r'colou?r'
        test_string = "color colour colouur"
        matches = re.findall(question_pattern, test_string)
        print(f"? pattern: {question_pattern}")
        print(f"Test string: '{test_string}'")
        print(f"Matches: {matches}\n")

def test_email_validator():
    """Test the email validator with various email addresses"""
    
    validator = EmailValidator()
    
    # Test cases: (email, expected_result, description)
    test_cases = [
        # Valid emails
        ("user@example.com", True, "Basic valid email"),
        ("test.email@domain.co.uk", True, "Email with dots and multiple TLD"),
        ("user+tag@example.org", True, "Email with plus sign"),
        ("user_name@example-domain.com", True, "Email with underscore and hyphen"),
        ("123@example.com", True, "Numeric local part"),
        
        # Invalid emails
        ("", False, "Empty email"),
        ("invalid", False, "No @ symbol"),
        ("@example.com", False, "Missing local part"),
        ("user@", False, "Missing domain"),
        ("user@domain", False, "Missing TLD"),
        ("user@.com", False, "Domain starts with dot"),
        ("user.@domain.com", False, "Local part ends with dot"),
        (".user@domain.com", False, "Local part starts with dot"),
        ("us..er@domain.com", False, "Consecutive dots in local part"),
        ("user@domain..com", False, "Consecutive dots in domain"),
        ("user@domain.c", False, "TLD too short"),
        ("user@@domain.com", False, "Multiple @ symbols"),
        ("user name@domain.com", False, "Space in local part"),
    ]
    
    print("=== EMAIL VALIDATION TESTS ===\n")
    
    passed = 0
    failed = 0
    
    for email, expected, description in test_cases:
        result = validator.validate_basic(email)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"{status} | {email:<25} | {description}")
        
        # Show detailed results for advanced validation
        if not result == expected or email == "user@example.com":
            is_valid, message = validator.validate_advanced(email)
            print(f"      Advanced validation: {message}")
        
        print()
    
    print(f"Test Results: {passed} passed, {failed} failed")
    return failed == 0

def interactive_email_validator():
    """Interactive email validation tool"""
    
    validator = EmailValidator()
    
    print("=== INTERACTIVE EMAIL VALIDATOR ===")
    print("Enter email addresses to validate (type 'quit' to exit)")
    print("Commands: 'demo' for regex demonstrations, 'help' for help\n")
    
    while True:
        try:
            user_input = input("Enter email: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            elif user_input.lower() == 'demo':
                validator.demonstrate_regex_patterns()
                continue
            elif user_input.lower() == 'help':
                print("\nCommands:")
                print("- Enter any email address to validate it")
                print("- 'demo' - Show regex pattern demonstrations")
                print("- 'quit' or 'exit' - Exit the program\n")
                continue
            elif not user_input:
                print("Please enter an email address or command.\n")
                continue
            
            # Validate the email
            is_valid_basic = validator.validate_basic(user_input)
            is_valid_advanced, message = validator.validate_advanced(user_input)
            
            print(f"\nEmail: {user_input}")
            print(f"Basic validation: {'✅ Valid' if is_valid_basic else '❌ Invalid'}")
            print(f"Advanced validation: {'✅' if is_valid_advanced else '❌'} {message}")
            
            # Show regex pattern breakdown
            print(f"\nPattern used: {validator.basic_pattern}")
            if is_valid_basic:
                # Extract parts using regex groups
                match = re.match(r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$', user_input)
                if match:
                    local, domain, tld = match.groups()
                    print(f"Local part: '{local}'")
                    print(f"Domain: '{domain}'")
                    print(f"TLD: '{tld}'")
            
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """Main program function"""
    
    print("Day 11: Regular Expressions - Email Validator")
    print("=" * 50)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        # Run tests
        success = test_email_validator()
        sys.exit(0 if success else 1)
    else:
        # Run interactive validator
        interactive_email_validator()

if __name__ == "__main__":
    main()