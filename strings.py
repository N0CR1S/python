print("Hello World!")
user = input("Coose your username: ")
passwd = input("Make a password: ")
login1 = input("Enter your username: ")
login2 = input("Enter your password: ")
if user == login1 and passwd == login2:
    user = user.strip().capitalize().title()
    # first, last = user.split()
    print("You are logged in!")
    # fstring to tell its formatted
    print(f"Welcome {user}!")
else:
    print("Wrong username or password!")
