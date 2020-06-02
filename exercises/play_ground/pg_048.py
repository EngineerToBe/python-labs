# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
