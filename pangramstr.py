Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string

def is_pangram(str):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(str.lower())

# Example Usage
input_str = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_str):
    print("The string is a pangram")
else:
    print("The string is not a pangram")
