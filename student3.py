import csv
name =input("whats your name")
home = input("whats your age")

with open("students2.csv","a") as file:
    writer = csv.writer(file)
    #writer function take file argument
    writer.writerow([name,home])

with open("students2.csv","a") as file:
    writer = csv.DictWriter(file,fieldname =["name","home"])
    #writer function take file argument
    writer.writerow(["name"== name,"home" == home])