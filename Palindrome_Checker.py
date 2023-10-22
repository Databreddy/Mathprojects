import re

def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    modified_string = re.sub(r'[^\w]', '', s).lower()
    # Check if the modified string is equal to its reverse
    return modified_string == modified_string[::-1]

# Example usage:
input_string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
