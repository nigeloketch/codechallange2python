# review.py
from customer import Customer
from Reasturantg import Restaurant

class Review:
    all_reviews = []
    id_counter = 1

    def __init__(self, rating, customer, restaurant):
        self.id = Review.id_counter
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        Review.id_counter += 1

    @classmethod
    def append_reviews(cls, review):
        cls.all_reviews.append(review)

    @classmethod
    def get_all_reviews(cls):
        for review in cls.all_reviews:
            print(f"Review ID: {review.id}")
            print(f"Rating: {review.rating}")
            print("Customer:")
            review.get_customer()
            print("Restaurant:")
            review.get_restaurant()
            print()

    def get_customer(self):
        print(self.customer.get_full_name())

    def get_restaurant(self):
        print(self.restaurant.get_name())
