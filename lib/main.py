from Customer import Customer
from Review import Review
from Restaurant import Restaurant

# Create instances
customer1 = Customer("George", "Washington")
customer2 = Customer("Uriah", "Smith")
restaurant1 = Restaurant("Ole Sereni")
restaurant2 = Restaurant("Hilton")

# Adding reviews
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Accessing data
print("Reviews for", restaurant1.get_name())
for review in restaurant1.get_reviews():
    print("  Rating:", review.get_rating(), "by", review.get_customer().given_name)

print("Customers who reviewed", restaurant1.get_name())
for customer in restaurant1.get_customers():
    print("  Customer:", customer.given_name)

# Calculate and print average star rating
print("Average star rating for", restaurant1.get_name(), ":", restaurant1.average_star_rating())

print("All reviews for", customer2.given_name)
for review in customer2.all_reviews:
    print("  Rating:", review.get_rating(), "for", review.get_restaurant().name)

print("Number of reviews for", customer2.given_name, ":", len(customer2.all_reviews))

# Find customer by name
found_customer = Customer.find_by_name("George", "Washington")
if found_customer:
    print("Found customer:", found_customer.full_name())
else:
    print("Customer not found.")

# Find all customers with a given name
customers_with_given_name = Customer.find_all_by_given_name("Uriah")
print("Customers with given name Uriah:")
for customer in customers_with_given_name:
    print("  Customer:", customer.full_name())
