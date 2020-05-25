# Boolean in Python
# True or False

# Delhi is India Capital city -- This is boolean as it is True

# Relational Operators

# The two boolean operators we’ll cover first are:

#    Equals: ==
#    Not equals: !=
#    Greater than: >
#    Less than: <
#    Greater than or equal to: >=
#    Less than or equal to: <=


# if condition
#     code

# Python function with if condition

def check_true(num1, num2):
    if num1 > num2:
        return True
    if num1 < num2:
        return False

print(check_true(10, 50))

# Boolean Operators
#  and
#  or
#  not

# For and
# True True   True
# True False  False
# False True  False
# False False False


# For or
# True True   True
# True False  True
# False True  True
# False False False


def i_am_py_func_and_or(x, y):
    if x == 10 and y == 10:
        return True
    if x == 10 or y < 10:
        return False

print(i_am_py_func_and_or(10, 10))

print(i_am_py_func_and_or(10, 9))

# there is one more way to write the above function 
# we can also use else statement with if

def i_am_py_func_with_else(x, y):
    if x > y:
        return x
    else:
        return y

print(i_am_py_func_with_else(10, 4))

print(i_am_py_func_with_else(30, 69))