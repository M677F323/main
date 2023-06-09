class wizard():
def __init__(self,name):
    def __init__(self,name):
        if not name:
            return ValueError("Missing Name")
        self.name = name
class Student(wizard):
def __init__(self,name,house):
    #if not name:
      #  return ValueError("Missing Name")
    #self.name = name
    self.house = house
class professor(wizard):
def __init__(self,name,subject)
    #if not name:
        #return ValueError("Missing Name")
    #self.name = name
    self.subject = subject

    