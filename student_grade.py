
# Student Marks and Grade Calculator

print("===== STUDENT GRADE CALCULATOR =====")

# Get student name
name = input("Enter student name: ")

# Get marks for 5 subjects
subject1 = float(input("Enter English marks: "))
subject2 = float(input("Enter Tamil marks: "))
subject3 = float(input("Enter Accounts marks: "))
subject4 = float(input("Enter Commerce marks: "))
subject5 = float(input("Enter Economics marks: "))

# Calculate total and average
total = subject1 + subject2 + subject3 + subject4 + subject5
average = total / 5

# Calculate grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

# Display result
print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", average, "%")
print("Grade:", grade)
