# SyntaxError
# print("Hello, World!)

'''
# ValueError
try:
    x = int(input("What's x? "))
#    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")

# NameError
#    print(f"x is {x}")

else:
    print(f"x is {x}")
'''

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # pass
            print("x is not an integer. Try again.")
        # else:
            # return x
            # break

main()
