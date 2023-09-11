""" names = []
 for i in range(3):
    name = input("whats your name? ")
    names.append(name) 
for _ in range(3):
    names.append(input("whats your name? "))
    
for name in sorted(names):
    print(f"Hello:{name}")
#this store only once and if we compile this it will ask again for the input this where the file I/O comes
#this will store the values which we have give """

#open to create or open a file  
# w= write file content 
#a- append
#file.write to open write name
#file.close()

""" name = input("whats your name? ")
file = open("names.txt","a")
file.write(f"{name}\n")
file.close()
 """
#with will write open and close for us

name = input("whats your name? ")
with open("names.txt","a") as file:
    file.write(f"{name}\n")