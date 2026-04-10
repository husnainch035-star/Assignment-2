# Take input from user
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

# Check if square or rectangle
if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")