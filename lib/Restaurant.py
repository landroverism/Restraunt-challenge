# Restaurant class definition

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.customers = []
        Restaurant.all_restaurants.append(self)

    # ... (other methods)

    def add_review(self, review):
        self.reviews.append(review)
        if review.customer not in self.customers:
            self.customers.append(review.customer)

    
