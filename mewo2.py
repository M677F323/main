#type hints
""" def meow(n):
    for _ in range(n):
        print("meow")

number = int(input("Number: "))
#TypeError: 'str' object cannot be interpreted as an integer so we do 
meow(number) """

""" def meow(n: int):#takes only int
    for _ in range(n):
        print("meow")

number : int = int(input("Number: "))# takes only int
meow(number) """#it works

def meow(n: int) -> str:
        return"meow\n" * n

number : int = int(input("Number: "))
meows :str = meow(number)
print(meows, end ="")#remove line form the end of last variable
#meow(number) this doent work because we are converting that into str