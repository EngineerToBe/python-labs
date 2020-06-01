# Write a function named count_char_x that takes a string named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

def count_char_x(word, x):
    count = 0
    for j in word:
        if j == x:
            count += 1
    return count

print(count_char_x("mississippi", "s"))
