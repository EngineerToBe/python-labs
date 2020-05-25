# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    elif len(lst1) < len(lst2):
        return lst2[-1]
    elif len(lst1) == len(lst2):
        return lst1[-1]

print(larger_list([1, 2, 3, 6], [4,5, 6]))
