class Review:
    all_reviews = []  # A list to keep track of all created review instances.

    def __init__(self, customer, restaurant, rating):
        # Initialize a new Review instance with the provided customer, restaurant, and rating.
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)  # Add the new review instance to the list of all reviews.

    def rating(self):
        return self._rating  # Return review

    def customer(self):
        return self._customer  # Return the customer associated with the review.

    def restaurant(self):
        return self._restaurant  # Return the restaurant associated with the review.

    @classmethod
    def all(cls):
        return Review.all_reviews  # Return