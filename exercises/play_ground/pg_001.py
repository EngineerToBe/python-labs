# Write a function named square_root() that has one parameter named num.
# Use exponents(**) to return the square root of num.

def square_root(num):
    if num == 0:
        return 0
    else:
        return num ** 0.5

result = square_root(5)

print(result)