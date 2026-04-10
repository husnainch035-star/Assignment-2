# Take ages as input from user
age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))

# Determine oldest
if age1 >= age2 and age1 >= age3:
    oldest = age1
elif age2 >= age1 and age2 >= age3:
    oldest = age2
else:
    oldest = age3

# Determine youngest
if age1 <= age2 and age1 <= age3:
    youngest = age1
elif age2 <= age1 and age2 <= age3:
    youngest = age2
else:
    youngest = age3

# Display results
print("Oldest age is:", oldest)
print("Youngest age is:", youngest)