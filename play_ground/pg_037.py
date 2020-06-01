# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

def max_num(nums):
    largest_num = nums[0]
    for num in nums:
        if num > largest_num:
            largest_num = num
    return largest_num


print(max_num([50, -10, 0, 75, 20]))
