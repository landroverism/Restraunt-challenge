from Customer import Customer
from Review import Review
from Restaurant import Restaurant

# Create instances
customer1 = Customer("George", "Washington")
customer2 = Customer("Uriah", "Smith")
restaurant1 = Restaurant("Ole Sereni")
restaurant2 = Restaurant("Hilton")

# Adding reviews needed
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Accessing my data
print(restaurant1.reviews)
print(restaurant1.customers)
print(restaurant1.average_star_rating())

print(customer2.all_reviews)  # Use 'all_reviews' instead of 'restaurants'
print(len(customer2.all_reviews))  # Use 'len(all_reviews)' instead of 'num_reviews'

# Find customer by name
found_customer = Customer.find_by_name("George", "Washington")
print(found_customer.full_name())

# Find all customers with a given name
customers_with_given_name = Customer.find_all_by_given_name("Uriah")
for customer in customers_with_given_name:
    print(customer.full_name())
