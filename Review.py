# Import the Customer and Restaurant classes from their respective modules
from customer import Customer
from Restaurant import Restaurant

# Define the Review class
class Review:
    # Class-level variables to store all reviews and an ID counter
    all_reviews = []
    id_counter = 0

    # Constructor to initialize a review object
    def __init__(self, rating, customer, restaurant):
        self.id = Review.id_counter  # Assign a unique ID to the review
        self.customer = customer  # Associate the review with a customer
        self.restaurant = restaurant  # Associate the review with a restaurant
        self.rating = rating  # Set the review's rating
        Review.all_reviews.append(self)  # Add the review to the list of all reviews
        Review.id_counter += 1  # Increment the ID counter

    # Class method to append reviews to the list of all reviews
    @classmethod
    def append_reviews(cls, review):
        cls.all_reviews.append(review)

    # Class method to get and print details of all reviews
    @classmethod
    def get_all_reviews(cls):
        for review in cls.all_reviews:
            print(f"Review ID: {review.id}")
            print(f"Rating: {review.rating}")
            print("Customer:")
            review.get_customer()  # Call the get_customer method to print customer details
            print("Restaurant:")
            review.get_restaurant()  # Call the get_restaurant method to print restaurant details
            print()

    # Instance method to get and print customer details
    def get_customer(self):
        print(self.customer.get_full_name())  # Call the get_full_name method of the customer

    # Instance method to get and print restaurant details
    def get_restaurant(self):
        print(self.restaurant.get_name())  # Call the get_name method of the restaurant
