def main():
    x = int(input("x: "))
    if parity(x):
        print("x is even")
    else:
        print("x is odd")

def parity(x):
    return x % 2 == 0

'''
def parity(x):
    if x % 2 == 0:
        return True
    else:
        return False
'''

main()
