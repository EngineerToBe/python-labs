# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
    if lst1 == lst2[-1:]:
        return True
    else:
        return False


#print(reversed_list([1, 5, 3], [3, 2, 1]))

lst1 = [1, 5, 3]
#print(lst1)
print(lst1[-1])