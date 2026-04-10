# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check greatest number
if num1 > num2:
    print("The greatest number is:", num1)
elif num2 > num1:
    print("The greatest number is:", num2)
else:
    print("Both numbers are equal.")