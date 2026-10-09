def main():
    hello()
    name = input("What's your name? ")
    hello(name)

# Default parameter value
def hello(to="world"):
    print("hello,", to)

main()
