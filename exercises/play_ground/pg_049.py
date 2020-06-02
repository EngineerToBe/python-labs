# A Spoonerism is an error in speech when the first syllables of two words are switched. 
# For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. 
# Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. 
# Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
    new_word1 = word1[0]
    new_word2 = word2[0]
    new_word3 = new_word2 + word1[1:]
    new_word4 = new_word1 + word2[1:]

    return new_word3 + " " + new_word4
