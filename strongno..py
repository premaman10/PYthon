Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> .  num = int(input("Enter a number: "))

# Find the factorial of each digit and sum the results
sum_of_factorials = 0
for digit in str(num):
    factorial = 1
    for i in range(1, int(digit) + 1):
        factorial *= i
    sum_of_factorials += factorial

# Check if the sum of factorials equals the input number
if sum_of_factorials == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")
