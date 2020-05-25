# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). 
# For example, every_three_nums(91) should return the list[91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
    list1 = []
    if start <= 100:
        list1 = list(range(start, 101, 3))
        return list1
        print(list1)
    elif start > 100:
        list1 = []
        return list1

print(every_three_nums(91))


list1 = list(range(90, 101, 3))

print(list1)
