""" with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}") """
#students = []
""" with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}") """
        #students.append(f"{name} is in {house}")
#for student in sorted(students):
#    print(student)


students = []
with open("students.csv") as file:
     #sorted according to line
    #for line in sorted(file):
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
#sort according to studnets name
""" def get_name(student):
    return student["name"]
def get_house(student):
    return student["house"]
for student in sorted(students, key = get_name): """
#by using lambda ananymous function
for student in sorted(students, key = lambda student :student["name"]):
    print(f"{student['name']} is in {student['house']}")