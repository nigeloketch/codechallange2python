
class Restaurant:
    def __init__(self, name):
        # Initialize a new Restaurant instance with the provided name.
        self._name = name
        self._reviews = []  # Initialize an empty list to store reviews for this restaurant.

    def name(self):
        return self._name  # Return the name of the restaurant.

    def reviews(self):
        return self._reviews  # Return a list of reviews for this restaurant.

    def customers(self):
        unique_customers = set()
        # Iterate through the reviews and collect unique customer instances.
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)  # Return a list of unique customer instances.

    def average_star_rating(self):
        total_ratings = 0
        num_reviews = len(self._reviews)
        if num_reviews == 0:
            return 0
        # Iterate through the reviews, summing up the ratings.
        for review in self._reviews:
            total_ratings += review.rating()
        return total_ratings / num_reviews  