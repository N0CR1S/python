students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ronald", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

'''
# lists
students = ["Harry", "Hermione", "Ronald", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
'''

'''
for student in students:
    print(student)
'''

'''
for i in range(len(students)):
   print(i + 1, students[i])
'''

'''
# dict -> dictionary
students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ronald": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")
'''
