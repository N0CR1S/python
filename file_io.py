# open, write, append, read, and with

name = input("What's your name? ")

# "a" appends, "w" overwrites, "r" reads
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Read line by line
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# Sorted names
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
