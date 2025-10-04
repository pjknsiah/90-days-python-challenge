'''
mission_name = "Sort"
chars = list(mission_name)
chars[0] = "P"
chars[-1] = "k"
updated_mission_name ='Is it okay to eat ' +  "".join(chars)

print(updated_mission_name)  # Pork
# This code will create a simplified fruit salad with the provided fruits
fruits = ['apple', 'banana', 'cherry', 'date']
fruits_in_salad = ""

index = 0
# Create a while loop that assembles a string of fruit names separated by spaces, without adding a space after the last fruit
# Hint: Consider using a conditional to determine when to add a space
while index < len(fruits):
    fruits_in_salad = " ".join(fruits)
    index += 1

# print(fruits_in_salad)  # Output the fruits in the salad
word = "FRUIT Salad"
non_vowels = 0
for char in word:
     if char in 'aeiouAEIOU ':
         continue
     else:
        non_vowels += 1
print(non_vowels)

# A simple text encryption exercise using the Caesar Cipher technique.
# The Caesar Cipher for `shift = 3` cyclically shifts every letter of the word by 3 positions:
# a -> d, b -> e, c -> f, ..., x -> a, y -> b, z -> c

#Implement the encryption logic by shifting each alphabet character

def encrypt_text(text):
    encrypted = ""
    for char in text:
        shift = 3
        if char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26
            encrypted += chr(ord('a') + shifted)
        elif char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26
            encrypted += chr(ord('A') + shifted)
        else:
            encrypted += char  # keep non-alphabet characters unchanged
    return encrypted

# Example text to encrypt
original_text = "Hello, Python!"
# The encrypted_text function call and print statement should be the same as in the solution
encrypted_text = encrypt_text(original_text)
print(encrypted_text)  # The correct output after implementing the TODO should be 'Khoor, Sbwkrq!'


def encrypt_text(text, shift_value):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            shifted_value = (ord(char) - ord("A") + shift_value) % 26
            encrypted_text += chr(ord("A") + shifted_value)
        elif char.islower():
            shifted_value = (ord(char) - ord("a") + shift_value) % 26
            encrypted_text += chr(ord("a") + shifted_value)
        else:
            encrypted_text += char

    print(encrypted_text)

encrypt_text("My Address is: 447 Melbourne High Street!", 1)

num_str = '123'
print(type(num_str)) # Output: <class 'str'>
num = int(num_str)
print(type(num)) # Output: <class 'int'>

numbers = '1,2,3,4,5'
# Convert string to a list of numbers
num_list = [int(number) for number in numbers.split(',')] 
print(num_list) # Output: [1, 2, 3, 4, 5]
# Calculate average
average = sum(num_list) / len(num_list)
print('The average is', average)  # Output: The average is 3.0

astronauts_data = "Buzz Aldrin, 1930;Yuri Gagarin, 1934;Valentina Tereshkova, 1937"

# Splitting the string into a list of astronaut info and stripping any whitespace
astronauts_list = astronauts_data.split(";")
cleaned_astronauts = []
print(astronauts_list)

for astronaut in astronauts_list:
    print(astronaut)
    parts = [ part.strip() for part in astronaut.split(',')]
    cleaned_astronauts.append(" ".join(parts))  # Modify this line to use the join() method

print(cleaned_astronauts)  # ['Buzz Aldrin 1930', 'Yuri Gagarin 1934', 'Valentina Tereshkova 1937']

def reversed_triple_chars(s: str) -> str:
    # TODO: Implement the function that reform the string as described above
    result = ""
    n = len(s)
    i = 0
    while i < n:
        triplet = s[i:i+3]
        result += triplet[::-1] if len(triplet) == 3 else triplet
        i += 3
    print(result)


reversed_triple_chars("PaulNsiahJunio")

def traverse_array(arr):
    """
    Traverse array starting from middle, alternating between left and right pairs.
    
    Args:
        arr: List of integers with odd length
        
    Returns:
        List of integers in the specified traversal order
    """
    n = len(arr)
    if n == 0:
        return []
    
    result = []
    middle_idx = n // 2
    
    # Start with middle element
    result.append(arr[middle_idx])
    
    # Initialize pointers for left and right sides
    left_ptr = middle_idx - 1
    right_ptr = middle_idx + 1
    
    # Alternate between taking pairs from left and right
    take_from_left = True
    
    while left_ptr >= 0 or right_ptr < n:
        if take_from_left and left_ptr >= 0:
            # Take up to 2 elements from the left side
            # Collect them first, then add in the original array order
            left_elements = []
            temp_ptr = left_ptr
            
            # Collect up to 2 elements moving outward
            for _ in range(2):
                if temp_ptr >= 0:
                    left_elements.append((temp_ptr, arr[temp_ptr]))
                    temp_ptr -= 1
                else:
                    break
            
            # Sort by index and add values in ascending index order
            left_elements.sort()
            for _, value in left_elements:
                result.append(value)
            left_ptr = temp_ptr
            
        elif not take_from_left and right_ptr < n:
            # Take up to 2 elements from the right side
            # Take them in normal order (closer to middle first)
            for _ in range(2):
                if right_ptr < n:
                    result.append(arr[right_ptr])
                    right_ptr += 1
                else:
                    break
        
        # Alternate sides
        take_from_left = not take_from_left
    
    return result


traverse_array([1, 2, 3, 4, 5, 6, 7])

def solution(s):
    groups = []
    current_group_char = None
    current_group_length = 0

    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    groups.append((current_group_char, current_group_length))
                current_group_char = char
                current_group_length = 1
    if current_group_char is not None:
        groups.append((current_group_char, current_group_length))
    
    print(groups)

solution("aabbccddddd")

def encode_rle(s):
    # TODO: implement
    result = []
    prev_char = ""
    char_len = 0
    for chr in s:
        if chr.isalnum():
            if chr == prev_char:
                char_len += 1
            else:
                if prev_char:
                    result.append(f"{prev_char}{char_len}")
                prev_char = chr
                char_len = 1
    if prev_char:
        result.append(f"{prev_char}{char_len}")
    
    return "".join(result)

def solution(s):
    # TODO: Implement the function here
    i = 0
    result = []
    n = len(s)
    while i < n:
        pair = s[i:i+2]
        count = 1
        while i + 2 < n and pair == s[i+2:i+4]:
            count += 1
            i += 2
        result.append(f"{pair}{count}")
        i += 2
    return "".join(result)

def solution(input_string):
    # TODO: implement your solution here
    s = input_string
    n = len(s)
    i = 0
    result = []
    while i < n:
        if s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            number = s[i:j]
            
            k = j
            while k < n and  not s[k].isalpha():
                k += 1
            
            if k < n:
                letter = s[k]
                result.append(letter + number)
                i = k + 1
            else:
                result.append(number)
                i = j
        else:
            result.append(s[i])
            i += 1
    return "".join(result)
'''
def count_minutes(period: str) -> int:
    # split start and end
    start_str, end_str = [p.strip() for p in period.split('-')]

    def to_seconds(t: str) -> int:
        h, m, s = map(int, t.split(':'))
        return h * 3600 + m * 60 + s

    start = to_seconds(start_str)
    end = to_seconds(end_str)

    # Find the first full minute after start
    if start % 60 == 0:
        first_minute = start
    else:
        first_minute = ((start // 60) + 1) * 60

    # Last full minute at or before end
    last_minute = (end // 60) * 60

    # If no valid minutes in between
    if first_minute > end:
        return 0

    # Count how many "minute ticks" between them
    return (last_minute - first_minute) // 60 + 1
