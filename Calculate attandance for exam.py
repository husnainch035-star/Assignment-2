# Take input from user
total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Display attendance percentage
print("Attendance percentage: {:.2f}%".format(attendance_percentage))

# Check if student is allowed to sit in exam
if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    print("Student is not allowed to sit in the exam.")