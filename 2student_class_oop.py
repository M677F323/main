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


""" #back to normal
#use of getter and setter class is if you are trying to change it will pass only from the setter function and it filter it
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
        #if I you self,_house then it will not go to the setter function
    def __str__(self):
        return f"{self.name} from {self.house}"
    #getter function only self
    #This is for house
    @property
    def house(self):
        return self._house
    #setter function self,house as input and set house
    @house.setter
    def house(self,house):
        if house not in ["guntur","vijaywada","banglore","Texas"]:
            raise ValueError("Invalid housename")
        self._house = house

    @property
    def name(self):
        return self._name
    @namesetter
    def name(self,name):
        if not name:
            return ValueError("Missing Name")
        return self._name
def main():
    student = get_student()
    #student.house = "kan"
    #student._house = "kan" unfortunately if passes even if you set setter and getter
    #in jave only we can prevent it
    #_ mean some thing is not important not to touch it _ _ is not at all to touch it
    print(student)
    
def get_student():
    name = input("Name :")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main() """

class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house
    
    def __str__(self,name):
        print(f"{self.name} is from {self.house}")
    
    @classmethod
    def get(cls):#creating class obj like that
        name = input("name: ")
        house = input("house")
        return cls(name,house)#makkiing or instantiating class variables
def main():
    student = get_student()
    print(student)
    
def get_student():
    name = input("Name :")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()