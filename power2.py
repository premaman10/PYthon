def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

num = int(input("Enter a number: "))

if is_power_of_two(num):
    print(num, "is a power of two")
else:
    print(num, "is not a power of two")
