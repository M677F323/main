#functions
def hello():
    print('hello')
name = input("what is your name? ")
hello()
print(name)


#functions if defined
def hello(to):
    print('hello,' to )
name = input("what is your name? ")
hello(name)

#functions if name is not defined
def hello(to="wolrd"):
    print('hello')
name = input("what is your name? ")
hello(name)

#functions
def main():
    name = input("what is your name? ")
    hello()

#functions
def hello(to = "world"):
    print(("hello," to))
   

main()

#return
def main():
    x= int(input("enter the value of x"))
    print("x squared is" square(x))

def square(n)
    return(n*n)

main(3)