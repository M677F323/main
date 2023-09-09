""" def main():
    x = int(input("Enter the value of X"))
    pyramid(x)

def pyramid(n):
    for i in range(n):
        print("x" * (i+1))
    
main() """

def main():
    x = int(input("Enter the value of X "))
    pyramid(x)

def pyramid(n):
    for i in range(n):
        print("x" * (i+1))
    

if __name__ == "__main__":
    main()