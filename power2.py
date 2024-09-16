Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

num = int(input("Enter a number: "))

if is_power_of_two(num):
    print(num, "is a power of two")
else:
    print(num, "is not a power of two")
