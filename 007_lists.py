# List's in Python
# A list is ordered set of objects/items
# 

# Empty List

names = []

# Integers List

numbers = [1, 34, 65, 67]

# Float List

float_numbers = [20.45, 56.89]

# String List

string_list = ['anay', 'vinu', 'vinayak']

# Mixed list

mixed_list = [1, 34.56, 'anay']

# List concatenation

new_lst = numbers + float_numbers + string_list + mixed_list

print(new_lst)

# List of List

list_of_list = [[1, 2], [3, 4], ['anay']]

# Python zip()
# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

name = ['Anay', 'Vinayak', 'Vinu']

age = [3, 4, 5]

birth_year = [2016, 2015, 2014]

new_list = zip(name, age, birth_year)

# see the output
print(new_list)

# see the output
print(list(new_list))

# List Method

age = [3, 4, 5]

# append
# to add 1 item at a time

age.append(6)

print(age)

# range

print(range(9))

# ranger start with 0 ends with 10 with difference of 2
range(0,11, 2)


# to get the length of the list 

len(age)

print(len(age))

# indexes in list

# Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

# Here are the index numbers for that list:

age = [2, 4, 6]
#      0  1  2

# to get the element from the list a particular index

age[0]
age[1]


# list slicing      

age = [1, 2, 3, 4, 6, 9]


age[0:3]

print(age[0:3])

# sort and sorted

age = [34, 54, 12, 32, 90, 45, 67, 78, 35]

# this changes the age and now when we print it will always return the sorted age
age.sort()

print(age)

# just in case if we dont want to change the original age list we can use sorted

age = [34, 54, 12, 32, 90, 45, 67, 78, 35]
age_sorted = sorted(age)


print(age)

print(age_sorted)

print(age)
