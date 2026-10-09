#not int but float to support decimals in digits
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

print("")
print("Press a for addition.")
print("Press s for subtraction.")
print("Press m for multiplication.")
print("Press d for division.")
print("")
operation = input()
print("")

def solution(solution=0):
    if solution == 0:
        print("Not a valid operation.")
    else:
        # :, for the commas
        print(f"{solution:,}")

if operation == "a":
    z = x + y
    solution(z)
elif operation == "s":
    z = x - y
    solution(z)
elif operation == "m":
    z = x * y
    solution(z)
elif operation == "d":
    if y == 0:
        print("You can't divide by zero")
    else:
        z = x / y
        solution(z)
else:
    solution()
