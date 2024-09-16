Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> .   num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print("The sum of digits is:", sum_of_digits)
