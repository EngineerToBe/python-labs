# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.

def remainder(num1, num2):
    result = (num1 * 2) % (num2 / 2)
    return result