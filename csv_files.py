import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# Write a row
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# Read rows
students = []
with open("students.csv") as file:
    reader = csv.DictReader(file, fieldnames=["name", "home"])
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# Sort with a lambda (anonymous function)
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
