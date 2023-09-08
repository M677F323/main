'''
x =int(input("whats the values of x"))

if x%2 == 0:
    print("Even")
else:
    print("Odd")
'''

def main():
    x =int(input("whats the values of x"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()