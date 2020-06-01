# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - 
# it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
  splits = word.split(x)
  print(splits)
  print(len(splits)-1)
  #return(len(splits)-1)


print(count_multi_char_x("apple", "pp"))
