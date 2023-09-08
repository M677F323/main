for _ in range(3):
    print("#")

##
def main():
    print_coloumn(3)

def print_coloumn(height):
    for _ in range(height):
        print("#")

main()

#can also written as
def print_coloumn(height):
    print("#\n" * height , end="")

main()