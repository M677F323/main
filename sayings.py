#This is create a functiona and use when ever we want

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello,{name}")
def goodbye(name):
    print(f"goodbye,{name}")

#main()
""" with this 
hello,world
goodbye,world
hello,veera """
#so we to get only hello sys.argv[1]  we can do  like this
if __name__ == "__main__":
    main()
#python sayinigmain.py veera
#hello,veera