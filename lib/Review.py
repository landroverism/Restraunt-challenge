class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating  # Renamed to 'rating_value'
        Review.all_reviews.append(self)

    def get_rating(self):  # Renamed method from 'rating' to 'get_rating'
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):  # Renamed method from 'customer' to 'get_customer'
        return self.customer

    def get_restaurant(self):  # Renamed method from 'restaurant' to 'get_restaurant'
        return self.restaurant
