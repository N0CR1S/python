# input, print, and string methods

name = input("What's your name? ")

# Remove whitespace and capitalize
name = name.strip().title()

# Split into first and last name
# first, last = name.split(" ")

print("Hello, ", end="")
print(name)
print(f"Hello, {name}")
print("Hello, " + name)
print("Hello,", name, sep=", ")
print("She said \"hello\"")
