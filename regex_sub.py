import re

url = input("URL: ").strip()

# Remove the prefix and keep only the username
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
