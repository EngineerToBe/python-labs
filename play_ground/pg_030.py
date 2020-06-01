# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

