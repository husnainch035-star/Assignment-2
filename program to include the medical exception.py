# Take input from user
total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

# Ask for medical cause
medical_cause = input("Do you have a medical cause? (Y/N): ").strip().upper()

# Calculate attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Display attendance percentage
print("Attendance percentage: {:.2f}%".format(attendance_percentage))

# Check eligibility
if attendance_percentage >= 75 or medical_cause == 'Y':
    print("Student is allowed to sit in the exam.")
else:
    print("Student is not allowed to sit in the exam.")