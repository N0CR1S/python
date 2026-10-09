# int, float, round, and number formatting

x = float(input("What's x? "))
y = float(input("What's y? "))

# Round to the nearest integer
z = round(x + y)
print(z)

# Thousands separator
print(f"{z:,}")

# Division, rounded to 2 decimals
z = round(x / y, 2)
print(z)

# Same result with f-string formatting
z = x / y
print(f"{z:.2f}")
