# Customer class definition

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.all_reviews = []

    # ... (other methods)

    def add_review(self, restaurant, rating):
        from Review import Review  # Import Review class here
        new_review = Review(self, restaurant, rating)
        self.all_reviews.append(new_review)
        restaurant.add_review(new_review)

    # ... (other methods)
