'''
i = 0
while i<=3:
    print("meow")
    i += 1
'''
'''
#for loop list of items
for i  in [0,1,2]:
    print("meow") #it will be in loooop

for i in range(3):
    print("meow")

#it can also be used to less space and make use of variable
for _ in range(3):
    print("meow")

#we can also write likethis  but line end with extra space
#print("meow\n"*3)

#print("meow\n"*3, end="") it remove space at the end of the 3rd meow
''' 
'''
# while loop if user give positive value loop break
while True:
    n = int(input("whats the n? "))
    if  n > 0:
        break
for _ in range(n):
    print("meow")
'''

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("whats the n? "))
        if  n > 0:
            break
    return n
def meow(n):
    for _ in range(n):
        print("meow")

