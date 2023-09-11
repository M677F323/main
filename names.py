names = []
""" for i in range(3):
    name = input("whats your name? ")
    names.append(name) """
for _ in range(3):
    names.append(input("whats your name? "))
    
for name in sorted(names):
    print(f"Hello:{name}")
#this store only once and if we compile this it will ask again for the input this where the file I/O comes
#this will store the values which we have give 