# Day 11: Email Validator using Regular Expressions

## What I Learned
- Basic regex patterns (\d, \w, \s, +, *, ?)
- Email validation logic
- Python re module usage

## How to Run
```bash
python email_validator.py

## 🔍 Debugging Tips

### Common Issues and Solutions:

1. **Pattern doesn't match**: Use regex101.com to test step by step
2. **Escaping problems**: Remember to escape special characters like `.`
3. **Greedy matching**: Understand how `+` and `*` work
4. **Case sensitivity**: Use flags like `re.IGNORECASE` if needed

### Testing Strategy:
```python
# Test with edge cases
test_cases = [
    ("", False),                    # Empty string
    ("a", False),                   # Too simple  
    ("a@b.c", False),              # TLD too short
    ("a@b.co", True),              # Valid minimal email
    ("very.long.email@example.com", True)  # Complex valid email
]