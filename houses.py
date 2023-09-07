students =[
    {"name":"veera","house":"guntur"},
    {"name":"ven","house":"vij"},
    {"name":"vira","house":"ban"},
    {"name":"keshav","house":"guntur"},
    {"name":"Kalyan","house":"guntur"}
]
""" houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
houses.sort()
print(houses) """
#it automatically sort and remove duplicates
houses = set()
for student in students:
    houses.add(student["house"])

