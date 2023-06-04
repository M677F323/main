""" class Student:
    ...
    #this mean we can implement later

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
# __ this is dunder
if __name__ == "__main__":
    main()
     """


# check with the user value but if empty italso create object
""" class Student:
    ...
    #this mean we can implement later
    def __init__(self,name,house,phn=None):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["guntur","vijaywada","banglore","Texas"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    name = input("Name :")
    house = input("House: ")
    #student = Student(name,house)
    #return student
    return Student(name,house)
if __name__ == "__main__":
    main()    """ 

""" class Student:
    ...
    #this mean we can implement later
    def __init__(self,name,house,phn=None):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["guntur","vijaywada","banglore","Texas"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
def main():
    student = get_student()
    #print(f"{student.name} from {student.house}")
    print(student)
def get_student():
    name = input("Name :")
    house = input("House: ")
    #student = Student(name,house)
    #return student
    return Student(name,house)
if __name__ == "__main__":
    main()  """  

""" #adding patronus
class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["guntur","vijaywada","banglore","Texas"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return f"{self.name} from {self.house}"
    def charm(self):
        match self.patronus:
            case "chard":
                return "🐶"
            case "otter":
                return "🐱"
            case "snake":
                return "🐍"
            case "lizard":
                return "🦎"
            case _:
                return "🪳"
            #or
            else:
                return "🦖"

def main():
    student = get_student()
    print("***patronus!***")
    print(student.charm())
    print(student)
def get_student():
    name = input("Name :")
    house = input("House: ")
    patronus = input("patronus: ")
    return Student(name,house,patronus)
if __name__ == "__main__":
    main()  """


#back to normal
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ["guntur","vijaywada","banglore","Texas"]:
            raise ValueError("Invalid housename")
        self._house = house

def main():
    student = get_student()
    #student.house = "kan"
    print(student)
    
def get_student():
    name = input("Name :")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()