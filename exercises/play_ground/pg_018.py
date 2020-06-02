# Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif 5 <= rating < 9:
        return "This one was fun."
    elif rating >= 9:
        return "Outstanding!"
