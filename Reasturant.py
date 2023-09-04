# Assuming you have already imported the Review class
from Review import Review

class Restaurant:
    def __init__(self, name):
        # Initialize a restaurant with a name
        self.name = name

    def get_name(self):
        # Return the restaurant's name
        return self.name

    def get_reviews(self):
        # Return a list of all reviews for this restaurant
        return [review for review in Review.reviews if review.get_restaurant() == self]

    def get_customers(self):
        # Return a unique list of customers who reviewed this restaurant
        customers = set()
        for review in self.get_reviews():
            customers.add(review.get_customer())
        return list(customers)

# Initialize a list to store restaurant instances
Restaurant.restaurants = []
