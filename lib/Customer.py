# Customer class definition

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all_reviews = []

    def add_review(self, restaurant, rating):
        from Review import Review  # Import Review class here
        new_review = Review(self, restaurant, rating)
        self.all_reviews.append(new_review)
        restaurant.add_review(new_review)

    @classmethod
    def find_by_name(cls, given_name, family_name):
        for customer in cls.all_customers:
            if customer.given_name == given_name and customer.family_name == family_name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name == given_name:
                matching_customers.append(customer)
        return matching_customers

    # ... (other methods)
