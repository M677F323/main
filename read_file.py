""" with open("names.txt","r") as file:
#readlines from file and store on lines
    lines = file.readlines()
for line in lines:
    #print("hello,",line)
    print("Hello,",line.strip()) """


""" #we can also write as 
#this can directly read line from file
with open("names.txt","r") as file:
    for line in file:
        print("hello,", line.rstrip()) """

names = []
""" #reading directly from file
#nonned to write"r" by deafule its r
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f'Hello, {name}') """

""" #reading and sorting direct file  as both at a time
with open("names.txt") as file:
    for line in sorted(file):
        print(f'hello,{line}')
 """

with open("names.txt") as file:
   for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello,{name}")