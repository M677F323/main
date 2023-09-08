x = 1
y = 2
z = x + y

print(z+1)



x = input("whats the value of x? ")
y = input("whats the value of y?")

print (x + y) # it represents 12 because it concatenate as string

#another way
i = int(input("whats the value of x? "))
l = int(input("whats the value of y? "))

print (i + l) # it represents 12 because it concatenate as string

#use tab to auto complete statement

#another way  hardest way but its possible
print((int(input("whats the value of x? "))) + (int(input("whats the value of y? "))))

#float
x = float(input("whats the value of x? "))
y = float(input("whats the value of y? "))

print(x+y)

#round(number[, ndigits]) using round method in documentation
#using round function
z = round(x+y)

print(f'{z:,}') #x=999 and y=1 o/p: 1,000
z = x / y
print(f'{z:,2f}') # round up to 2 decimals x=2,y=3 o/p 0.67




