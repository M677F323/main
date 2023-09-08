def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#",end='')
        print()#once loop is done go to next line like \n
        

main()
# another way
def print_square(size):
    #for each row in square
    for i in range(size):
        print("#" * size)
main()


#if you dont understand
def main():
    print_sqaure(3)

def print_sqaure(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()


