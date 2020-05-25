# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. 
# Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"

def dog_years(name, age):
    result = name + "," + " you are " + str(7*age) + " years old in dog years"
    return result

