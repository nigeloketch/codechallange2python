# Define a Python class named Restaurant.
class Restaurant:
    # The constructor method (__init__) initializes the object with a 'name' attribute.
    def __init__(self, name):
        self.name = name  # Store the 'name' attribute when creating a new instance.

    # A method to get the name of the restaurant.
    def get_name(self):
        return self.name  # Return the 'name' attribute of the instance.
