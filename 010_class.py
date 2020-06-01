# A class in Python is template

# to define class

class Name:
    pass

# A class must be instantiated. In other words, we must create an instance of the class, in order to breathe life into the schematic.
# Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined Name as follows:
# A class instance is also called as object

name1 = Name()

# when we want to share data or make data available to different instances of class we can create a class variable or attribute

# define a class

class Name:
    name = 'anay'  # class variable or attribute
    
# instance of the class

name1 = Name()

print(name1.name)

# Methods are nothing but a Python function but are defined under class.
# The first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self. 
# Methods always have at least this one argument.


class Name:
    name = 'anay'  # class variable or attribute

    def print_message(self):
        print(Name.name+ 'Good Day' )

# instance of the class


name1 = Name()

print(name1.print_message)

# Python constructors or dunder methods



