def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum1 = sum_of_divisors(num1)
sum2 = sum_of_divisors(num2)

if sum1 == num2 and sum2 == num1:
    print(num1, "and", num2, "are amicable numbers")
else:
    print(num1, "and", num2, "are not amicable numbers")
