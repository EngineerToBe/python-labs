# Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end(inclusive) have been removed.
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

#remove_middle([4, 8, 15, 16, 23, 42], 1, 3)

def remove_middle(lst, start, end):
    list_new = lst[0:start] + lst[1 + end:]
    return list_new


def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]


remove_middle([4, 8, 15, 16, 23, 42], 1, 3)
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
    

list1 = [4, 8, 15, 16, 23, 42]

list_new = list1[0:1] + list1[4:]

print(list_new)
