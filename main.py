from customer import Customer
from restaurant import Restaurant
from review import Review


# customers
customer1 = Customer("Elvis", "kroy")
customer2 = Customer("Nigel", "King")
customer3 = Customer("Bruce", "Lee")
customer4 = Customer("Jonathan", "Glog")
customer5 = Customer("Blue", "Ape")

# Restaurants
res1 = Restaurant("Pronto")
res2 = Restaurant("jackeats")
res3 = Restaurant("king burger")

# review of restaurants
customer1.add_review(res1, 5)
customer2.add_review(res2, 1)
customer3.add_review(res1, 3)
customer4.add_review(res2, 2)
customer5.add_review(res3, 4)

# ratings for the restaurant
avg_rating_res1 = res1.average_star_rating()
print(f"Average star rating for {res1.name()}: {avg_rating_res1:.2f}")

avg_rating_res3 = res3.average_star_rating()
print(f"Average star rating for {res3.name()}: {avg_rating_res3:.3f}")

# list of all customers to be displayed
all_customers = Customer.all()
print("All customers:")
for customer in all_customers:
    print(customer.full_name())

# Display a list of all reviews
all_reviews = Review.all()
print("All reviews:")
for review in all_reviews:
    print(f"Customer: {review.customer().full_name()}, Restaurant: {review.restaurant().name()}, Rating: {review.rating()}")