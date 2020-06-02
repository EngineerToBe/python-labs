# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print d subtracted from c.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed mod a.

def lots_of_math(a, b, c, d):
    first_num = a + b
    print(first_num)
    second_num = c - d
    print(second_num)
    third_num = first_num * second_num
    print(third_num)
    return third_num % a
    
