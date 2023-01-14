

"""these are the ****doc strings***
    these we can write middle of the codes and we have certain tools we can use that tools and analyse the code and 
    we can create the documentation with these strings automatically by these comments not "#" 
    only this ->
    i will keep every uniformly indented  
    
    : """

#the  decalaration of doc sting like  below
def meow(n: int) -> str:
    """
    this is contion known as "restructured text"
    third aprt tools can create documnetation fo rthis code if we decalare
    Meow n times
    :param n :numbers oftime it return
    :type n: int
    :raise TypeError :if input is not int 
    :return :A string of n meows at aline
    :rtype :str

    """
        return"meow\n" * n

number : int = int(input("Number: "))
meows :str = meow(number)
print(meows, end ="")