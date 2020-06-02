# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

def first_three_multiples(num):
    if num == 0:
        return 0
    else:
        print(num * 1)
        print(num * 2)
        print(num * 3)
        return num * 3