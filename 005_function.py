# A fucntion is a way to arrange the logic and can be reusable

# in Python we can write a function 

# def myyfirstfunc():
#    code

# first function

# Python function with no parameters

def your_name():
    print('My name is Anay Amralkar')


# to call a function

your_name()

# Python function with 1 parameter

def your_name_1_arity(name):
    print('My name is ' + name)

your_name_1_arity('Anay') 


# Python function with multiple parameters

def i_am_py_func_multi_par(num, x, y):
    print(num + (x * y))

i_am_py_func_multi_par(10, 40, 55)


# Python function with keywords argument
# 
def func_key_word_arg(x, y=10):
    print("The value of X is " + str(x) + " and the value of Y is" + str(y))


# the x and y are integers and we wrap them around str() to convert them as a string
# if we dont do it the function returns TypeError
# keyword argument be never the first 

func_key_word_arg(10)
func_key_word_arg(10, 20)        


# return in Python function
# Printing and returning are completely different concepts.
# print is a function you call. Calling print will immediately make your program write out text for you to see. Use print when you want to show a value to a human.
# return is a keyword. When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called. 
# Use return when you want to send a value from one point in your code to another.
# Using return changes the flow of the program. Using print does not.

def py_func_with_return(x, y):
    return x ** y

# this will not output anything
py_func_with_return(3, 6)

# but this will
print(py_func_with_return(3, 6))


# multiple return

def py_func_with_multi_return(x, y):
    sum = x + y
    multi = x * y
    return sum, multi


two_num_sum, two_num_multiplication = py_func_with_multi_return(100, 400)


print(two_num_sum)
print(two_num_multiplication)



