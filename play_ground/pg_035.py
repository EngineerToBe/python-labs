# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num1 in lst1:
        sum1 += num1
    for num2 in lst2:
        sum2 += num2
    if sum1 > sum2:
        return lst1
    elif sum2 > sum1:
        return lst2
    elif sum1 == sum2:
        return lst1


print(larger_sum([1, 9, 5], [2, 3, 7]))
