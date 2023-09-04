# customer.py

class Customer:
    all_customers = []
    id_counter = 0
#initialize the object
    def __init__(self, first_name, last_name):
        self.id = Customer.id_counter
        self.first_name = first_name
        self.last_name = last_name
        Customer.all_customers.append(self)
        Customer.id_counter += 1

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
