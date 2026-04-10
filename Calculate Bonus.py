# Take input from user
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Check condition and calculate bonus
if years_of_service > 5:
    bonus = salary * 0.05
else:
    bonus = 0

# Display result
print("Your bonus amount is:", bonus)