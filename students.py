""" with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}") """
#students = []
with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        #students.append(f"{name} is in {house}")
#for student in sorted(students):
#    print(student)


students = []
with open("students.csv") as file:
     #sorted according to line
    #for line in sorted(file):
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        #creating empty dictionary
"""     student = {}
        student["name"] =name
        student["house"]=house """
        student = {"name":name, "house":house}
        students.append(student)
for student in students:
    print{f"{student['name']} is in {student['house']}"}