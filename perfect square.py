import math

def find_perfect_squares(start, end):
    perfect_squares = []
    for i in range(start, end+1):
        sqrt = math.sqrt(i)
        if sqrt == int(sqrt):
            perfect_squares.append(i)
    return perfect_squares

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

perfect_squares = find_perfect_squares(start, end)

print("The perfect squares between", start, "and", end, "are:", perfect_squares)
