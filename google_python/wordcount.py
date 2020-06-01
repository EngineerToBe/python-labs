#!/usr/bin/python3 -tt

def print_words(filename):
  d = dict()                                 
  with open(filename) as file:
    for line in file:
      line = line.strip()
      line = line.lower()
      words = line.split(" ")
      for word in words:
        if word in d:
          d[word] = d[word] + 1
        else:
          d[word] = 1
    for key in list(d.keys()):
      print(key, ":", d[key])


print(print_words("/home/aaa/Code/Python/codeacademy/google_python/clown.txt"))
