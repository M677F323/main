email = input("Enter the email? ").strip()
""" 
if  "@" in email and "." in email:
    print("valid")
else:
    print("invalid") """

username, domain = email.split("@")
#if username and "." in domain:
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")