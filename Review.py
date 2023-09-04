class Review:
    def __init__(self, customer, restaurant, rating):
        # Initialize a review .
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_rating(self):
        # rating for this review being returned
        return self.rating

    @classmethod
    def get_all_reviews(cls):
        # Return all review 
        return cls.reviews

    def get_customer(self):
        # Return the customer object for this review
        return self.customer

    def get_restaurant(self):
        # Return the restaurant object for this review
        return self.restaurant


# Initialize a list to store review instances
Review.reviews = []
