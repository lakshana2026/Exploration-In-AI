# Student Record Management with List, Tuple, Dictionary and CSV
import csv

# Modified student records list
students = [
    {"RollNo": "104", "Name": "Dinesh", "Department": "AI&DS", "Mark": 89},
    {"RollNo": "105", "Name": "Elango", "Department": "CSE", "Mark": 94},
    {"RollNo": "106", "Name": "Farhana", "Department": "ECE", "Mark": 82}
]

# Tuple example: fixed course details
course = ("Data Structures", 3)
print("Course Tuple:", course)

# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"], row["Department"], row["Mark"])