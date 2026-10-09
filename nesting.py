def main():
    print_cube(3,3)

def print_cube(width, height):

    # For each row in cube
    for i in range(height):
        
        # Print brick for each brick in row
        print(" # " * (width))

main()
