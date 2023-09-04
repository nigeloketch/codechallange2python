# main.py
from customer import Customer
from Review import Review
from Restaurant import Restaurant

# Create a customer
customer1 = Customer("John", "Doe")

# Create a restaurant
restaurant1 = Restaurant("Pronto")

# Create a review and associate it with the customer and restaurant
review1 = Review("Good", customer1, restaurant1)

# Get and print the customer's full name and restaurant name from the review
review1.get_customer()
review1.get_restaurant()


(Review.get_all_reviews())



