def main():
    x = int(input("whats the value of x ? "))
    print("x is ", square(x))

def square(n):
    return n * n

#3 sqaure is not 9 n+n
#if we use assert  the for this  we get assertion error

#main()
if __name__ == "__main__":
    main()