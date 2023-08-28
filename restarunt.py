class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        customer_list = []
        for review in self.reviews:
            customer = review.customer()
            if customer not in customer_list:
                customer_list.append(customer)
        return customer_list


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        restaurant.reviews.append(self)
        customer.reviews.append(self)

    def rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
