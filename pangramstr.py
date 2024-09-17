import string

def is_pangram(str):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(str.lower())

# Example Usage
input_str = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_str):
    print("The string is a pangram")
else:
    print("The string is not a pangram")
