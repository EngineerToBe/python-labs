# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

def win_percentage(wins, losses):
    total = wins + losses
    percentage_won = (total - losses) * 10
    return percentage_won


print(win_percentage(10, 0))
