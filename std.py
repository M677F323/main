""" import csv

students = []

# Configure the csv reader to handle multiple commas and newlines within a field
with open("students.csv") as file:
    reader = csv.reader(file)
    for name,home in reader:
            name, home =  students.append({"name": name, "home": home})
# Sort and print the students
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}") """


import csv
students = []

# Configure the csv reader to handle multiple commas and newlines within a field
with open("students2.csv") as file:
    #returnd dictionaries
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
# Sort and print the students
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
#this using DictReader and we can change it if we change colum also it works accordings to the csv file
house