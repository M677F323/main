#print function is predefined to print a variable or string
#argumets we are passing to the function
print("hello world")

# Take input form the user
name = input("whats your name: ")

#concatanating name to string
print("Hello," + name) 
"""
string in python is str
*objecst mean any no of strings we can take
sep='', default seperate by the single space
end='\n' its default
print(*objetcs, sep='', end='\n', file=sys.stdout, flush =False)
we can over ride those like  end="" then it will not move to next line
"""
name = name.strip() #eliminate the white spaces front and end we can also use lstrip() and rstrip()
name = name.capitalize() #it like  Veera sekhar only first letter is capital
name = name.title() #make every frist letter capital like Veera Sekhar

#we can also combine all of them like below this
name = name.strip().title()

#and als0 we can also do like this
name = input("whats you name? ").strip().title()

#splitting and assigning the names
first,last = name.split("")
print('hello,"world"')

#we can use back slashes so it think that it is sub literal ot sub string ( \"  \ " )
print('hello,\"world\"')

#another way to import or format name
print(f"hello, {name}")



