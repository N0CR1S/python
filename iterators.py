students = ["Hermione", "Harry", "Ron"]

# What a for loop does under the hood
iterator = iter(students)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# next(iterator) would now raise StopIteration
