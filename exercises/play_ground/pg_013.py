# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo ( % ) to check for divisibility.

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False