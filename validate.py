#valiadting  email
import sys
import csv
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

#re regular expresions library

""" if len(sys.argv) > 1:
    email = sys.argv[1]
    with open("email.txt","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email]) 
 """

import sys
import csv

if len(sys.argv) > 1:
    email = sys.argv[1]  # Assuming the email address is the first command-line argument
    with open("email.txt", "a") as file:
        writer = csv.writer(file)
        writer.writerow([email])
else:
    print("Usage: python validate.py <email>")