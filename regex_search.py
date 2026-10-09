# docs.python.org/3/library/re.html

import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
    print("Valid")
else:
    print("Invalid")
