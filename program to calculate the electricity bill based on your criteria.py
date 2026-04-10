# Take number of units as input from user
units = int(input("Enter number of units consumed: "))

# Initialize bill amount
bill = 0

# Calculate bill based on units
if units <= 100:
    bill = 0
elif units <= 300:  # Next 200 units
    bill = (units - 100) * 5
else:  # Units above 300
    bill = (200 * 5) + ((units - 300) * 10)

# Display total bill
print("Total electricity bill: Rs.", bill)