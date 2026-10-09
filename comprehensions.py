students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name": name, "house": "Gryffindor"} for name in students]
print(gryffindors)

# List comprehension with a condition
words = ["This", "is", "CS50"]
uppercased = [word.upper() for word in words]
short = [word for word in words if len(word) <= 2]
print(uppercased, short)

# Dictionary comprehension
gryffindors = {name: "Gryffindor" for name in students}
print(gryffindors)
