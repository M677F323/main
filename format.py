imprt re
name = input("whats your name? ").strip()
""" if , in name:
    last, first = name.split(",")
    name = f"{first}{last}"
print(f"hello,{name}") """
matches =re.search(r"^().+), (.+)$", name)
if matches:
    last ,first = matches.groups()
    name = f"{first} {last}"
print(f"hello {name}")