students ={
            "hermin" :"grfyin",
            "hyrii" : "uiin",
            "vere" : "uyyyt",
            "onn" : "yywte"
}
#keys and values
print(students["hermin"])
#paper and pencil

# looop
for i in students:
    print(i,students[i])

#another way
students = {
    "John": 90,
    "Alice": 85,
    "Bob": 88,
}

for name, score in students.items():
    print(f"{name}: {score}")

#lists
students =[ 
    {"name":"veera","age":20,"group":"a"},
    {"name":"sridhar","age":40,"group":"b"},
    {"name":"dherraj","age":24,"group":"c"},
    {"name":"nav","age":33,"group":None}
    ]
for i in students:
    print(i["name"],i["age"],i["group"], sep=',')
