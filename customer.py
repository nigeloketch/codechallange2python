class Customer:
    def __init__(self, given_name, family_name):
        # Initialize a customer with given name and family name
        self.given_name = given_name
        self.family_name = family_name

    def get_given_name(self):
        # Return the customer's given name
        return self.given_name

    def get_family_name(self):
        # Return the customer's family name
        return self.family_name

    def get_full_name(self):
        # Return the full name of the customer
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def get_all_customers(cls):
        # Return all customer instances
        return cls.customers


# Initialize a list to store customer instances
Customer.customers = []
