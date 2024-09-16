Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> .  def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum1 = sum_of_divisors(num1)
sum2 = sum_of_divisors(num2)

if sum1 == num2 and sum2 == num1:
    print(num1, "and", num2, "are amicable numbers")
else:
    print(num1, "and", num2, "are not amicable numbers")
