# with loops we can perform the set of task for n number of times

# for loop

pandavas = ['Yudhisthir', 'Arjun', 'Bhim', 'Nakul', "Sahdev"]

for pandav in pandavas:
    print(pandav)


# break and continue
# The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
# If the break statement is inside a nested loop(loop inside another loop), the break statement will terminate the innermost loop.

for pandav in pandavas:
    if pandav == 'Bhim':
        print("My fav Pandav")
        break

# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

kids_age = [10, 9, 12, 14, 18, 13]

for age in kids_age:
    if age < 10:
        continue
    else:
        print(age)

# while loop
# The while loop performs a set of code until some condition is reached.
# While loops can be used to iterate through lists, just like for loops:

# List comprehensions are a third way of making lists. 
# With this elegant approach, you could rewrite the for loop from the first example in just a single line of code:


ages = [23, 45, 67, 87, 100, 12, 14]

adult_age = [age for age in ages if age >= 18]

print(adult_age)