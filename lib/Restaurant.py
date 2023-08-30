# Restaurant class definition

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.customers = []
        Restaurant.all_restaurants.append(self)

    def add_review(self, review):
        self.reviews.append(review)
        if review.customer not in self.customers:
            self.customers.append(review.customer)

    def average_star_rating(self):
        total_ratings = sum([review.get_rating() for review in self.reviews])
        if len(self.reviews) > 0:
            return total_ratings / len(self.reviews)
        else:
            return 0

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return self.customers
