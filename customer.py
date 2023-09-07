from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer.all_customers.append(self)  # Add the new customer instance to the list of all customers.

    def given_name(self):
        return self._given_name  # Return the given name of the customer.

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers  # Return a list of all customer instances.

    def restaurants(self):
        unique_restaurants = set()
        # Go through the customer's reviews and gather a list of unique restaurant names
        for review in self._reviews:
            unique_restaurants.add(review.restaurant())
        return list(unique_restaurants)  # Return a list of unique restaurant names.

    def add_review(self, restaurant, rating):
        # Instantiate a new Review object linked to this customer, the restaurant, and the given rating.
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)