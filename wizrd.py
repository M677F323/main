class wizard():
def __init__(self,name):
        if not name:
            return ValueError("Missing Name")
        self.name = name
#inheritance like (wizard)
#super().__init__()
class Student(wizard):
def __init__(self,name,house):
    #if not name:
      #  return ValueError("Missing Name")
    #self.name = name
    super().__init__(name)
    self.house = house
class professor(wizard):
def __init__(self,name,subject)
    #if not name:
        #return ValueError("Missing Name")
    #self.name = name
    super().__init__(name)
    self.subject = subject

    