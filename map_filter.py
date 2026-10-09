words = ["This", "is", "CS50"]

# map applies a function to every item
uppercased = map(str.upper, words)
print(*uppercased)

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# filter keeps items where the function returns True
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for student in sorted(gryffindors, key=lambda s: s["name"]):
    print(student["name"])
