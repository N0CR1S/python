# docs.python.org/3/library/sys.html

import sys

# Check for errors.

if len(sys.argv) < 2:
    sys.exit("Too few arguments!")

# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments!")

# Print the name.

# print("Hello, my name is", sys.argv[1])

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Hello, World!")
