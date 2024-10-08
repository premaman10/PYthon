n = int(input("Enter a number: "))

# initialize the first two terms of the series
a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    print("Fibonacci sequence up to", n, ":")
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a, b = b, c
        if c <= n:
            print(c)
        else:
            break
