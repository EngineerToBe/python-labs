# Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False