# Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 20 characters long. 
# If word is already at least 20 characters long, just return word.


def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word


import random


#numbers_b = random.randint(range(0, 1000, 12))

numbers_a = random.choice(range(1, 1000, 12))

print(numbers_a)
