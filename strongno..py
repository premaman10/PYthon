num = int(input("Enter a number: "))

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
