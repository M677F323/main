import random
class Hat:

    def __init__(self):
        self.houses = ["guntur","vijayawada","Texas","Austin","europe"]
    def sort(self,name):
        print(name ,"is in ",random.choice(self.houses))

hat = Hat()
hat.sort("harry")


""" #even normally we cn write but when code become complicated then we cannt maage it
import random
self.houses = ["guntur","vijayawada","Texas","Austin","europe"]
def sort(name):
    print(name ,"is in ",random.choice(houses))
hat.sort("harry") """