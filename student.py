""" name = input("Name:")
house = input("house")
print(f"{name} from {house}") """

""" def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
def get_name():
    return input("Name:")
def get_house():
    return input("House:")
if __name__ == "__main__":
    main() """

""" def main():
    name,house = get_student()

    print(f"{name} from {house}")
def get_student():
    name = input("Name: ")
    house = input("house: ")
    return name,house
if __name__ == "__main__":
    main() """

""" def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    #print(f"{name} from {house}")
def get_student():
    name = input("Name: ")
    house = input("house: ")
    #return tuple
    return (name,house)
if __name__ == "__main__":
    main() """

""" def main():
    student ={}
    student = get_student()
    print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("Name: ")
    house = input("house: ")
    return name,house
if __name__ == "__main__":
    main()
 """
"""  def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("Name: ")
    house = input("house: ")
    return name,house
if __name__ == "__main__":
    main() """

""" def main():
    student = get_student()
    if student[0] == "veera":
        student[1] = "vijayawada"
    print(f"{student[0]} from {student[1]}")
def get_student():
    name = input("Name: ")
    house = input("house: ")
    return [name,house]
if __name__ == "__main__":
    main() """

#Its clear that name is name no need to remember
""" def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")
def get_student():
    student= {}
    student["name"] = input("Name: ")
    student["house"] = input("house: ")
    return student
if __name__ == "__main__":
    main()  """

def main():
    student = get_student()
    if student["name"] == "veera":
        student["house"] = "vijayawada"
    print(f"{student['name']} from {student['house']}")
def get_student():
    name = input("Name: ")
    house = input("house: ")
    return {"name":name, "house":house}
if __name__ == "__main__":
    main()