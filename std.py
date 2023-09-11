import csv

students = []

# Configure the csv reader to handle multiple commas and newlines within a field
with open("students.csv") as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        if len(row) >= 2:
            name, home = row[:2]  # Only consider the first two values (name and home)
            students.append({"name": name, "home": home})

# Sort and print the students
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")



#as dict reader
students = []

# Configure the csv reader to handle multiple commas and newlines within a field
with open("students.csv") as file:
    reader = csv.DictReaderreader(file, delimiter=',', quotechar='"')
    for row in reader:
        if len(row) >= 2:
            name, home = row[:2]  # Only consider the first two values (name and home)
            students.append({"name": name, "home": home})

# Sort and print the students
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")