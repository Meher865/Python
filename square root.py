import math
num = float(input("Enter a number to find the square root: "))
if num < 0:
    print("Square root is not defined for negative numbers.")
else:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")