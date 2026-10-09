def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How much meow? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

'''
###
i = 0
while i < 10:
    print("meow")
    i += 1
###
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("meow")
###
# _ to dont use a variable
for _ in range(10):
    print("meow")
###
print("meow\n" * 10, end = "")
###
while True:
    n = int(input("Want more? "))
#
    if n < 0:
        continue
    else:
        break
#
    if n > 0:
        break
for _ in range(n):
    print("meow")
###
'''
