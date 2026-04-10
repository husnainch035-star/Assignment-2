# Take quantity as input from user
quantity = int(input("Enter quantity: "))

# Cost per unit
price_per_unit = 100

# Calculate total cost
total_cost = quantity * price_per_unit

# Apply discount if applicable
if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost = total_cost - discount

# Display final cost
print("Total cost to be paid:", total_cost)