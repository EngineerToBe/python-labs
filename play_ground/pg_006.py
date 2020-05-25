# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
    amount = total / 100 * percentage
    return amount

print(tip(10, 25))