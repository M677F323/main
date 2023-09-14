class Vault:
    def __init__(self,galleons=0, sickles=0,knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return (f"{self.galleons}galleons and {self.sickles}sickles and {self.knuts}knuts")
#join two lists 
    def __add__(self,other):
        galleons = self.galleons+other.galleons
        sickles = self.sickles+other.sickles
        knuts = self.knuts+other.knuts
        return Vault(galleons,sickles,knuts)

potter = Vault(100,20,23)
print(potter)

wasley = Vault(200,18,34)
print(wasley)

""" galleons =potter.galleons+wasley.galleons
sickles = potter.sickles+wasley.sickles
knuts= potter.knuts+wasley.knuts

total = Vault(galleons,sickles,knuts)
print(total) """
#for this it act as similar way and add them
#total =(self+other)
total = potter + wasley
print(total)