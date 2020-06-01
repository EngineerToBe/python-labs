# A dictionary is an unordered set of key: value pairs.

family = {"father_name": "Abhishek", "son_name": "Anay"}

# empty dictionary

dict1 = {}

# to add k:v (key:value) pairs to dictionaries

dict1["name"] = 'Anay'
dict1["surname"] = 'Amralkar'

print(dict1)

# to add multiple k:v's

dict1.update({"nickname": 'Vinu', "school": "DGS"})

print(dict1)

# update the existing values

dict1["surname"] = 'Amral'

# list comprehensions in dictionaries

names = ['anay', 'vinu', 'vinayak', 'jhampudi']
sports = ['cycling', 'boxing', 'football', 'cricket']

hobby = {key: value for key, value in zip(names, sports)}

print(hobby)

# get method to get the value for the key

hobby_new = hobby.get('anay')
print(hobby_new)

# get with dfault value if key dont exist

hobby_new1 = hobby.get('abhishekj', 'programming')