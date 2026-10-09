def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

# yield returns one value at a time instead of building a whole list
def sheep(n):
    for i in range(n):
        yield "🐑" * i

main()
