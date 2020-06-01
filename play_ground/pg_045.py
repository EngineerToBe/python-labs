# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
# This function should return True if every word in sentence has a length greater than or equal to x.


def x_length_words(sentence, x):
  words = sentence.split(" ")
  print(words)
  for word in words:
    if len(word) < x:
      return False
  return True


print(x_length_words("he likes apples", 2))
