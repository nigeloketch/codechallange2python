class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def all(self):
        return self

    def restaurants(self):
        restaurant_list = []
        for review in self.reviews:
            restaurant = review.restaurant()
            if restaurant not in restaurant_list:
                restaurant_list.append(restaurant)
        return restaurant_list

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)


class Review:
    ...
