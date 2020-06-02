# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

def add_greetings(names):
    lst1 = ["Hello " + name for name in names]
    return lst1


print(add_greetings(["Owen", "Max", "Sophie"]))
