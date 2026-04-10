# Take input from user
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").strip().upper()
marital_status = input("Enter marital status (Y/N): ").strip().upper()  # Though not used in rules

# Check conditions and print place of service
if gender == 'F':
    print("Place of service: Urban areas only")
elif gender == 'M':
    if 20 <= age <= 40:
        print("Place of service: Anywhere")
    elif 40 < age <= 60:
        print("Place of service: Urban areas only")
    else:
        print("ERROR")
else:
    print("ERROR")