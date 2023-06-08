class Wizard:
    def __init__(self,name):
        if not name:
            return ValueError("Missing Name")
        self.name = name
#inheritance like (wizard)
#super().__init__()
class Student(Wizard):
    def __init__(self,name,house):
        #if not name:
        #  return ValueError("Missing Name")
        #self.name = name
        super().__init__(name)
        self.house = house
class Professor(Wizard):
    def __init__(self,name,subject):
        #if not name:
            #return ValueError("Missing Name")
        #self.name = name
        super().__init__(name)
        self.subject = subject

wizard = Wizard("veera")
student = Student("kin","china")
professor = Professor("malen","cs50")

