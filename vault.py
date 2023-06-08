class Vault:
    def __init__(self,galleons=0, sickles=0,knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return (f"{self.galleons}galleons and {self.sickles}sickles and {self.knuts}knuts")
potter = Vault(100,20,23)
print(potter)

wasley = Vault(200,18,34)
print(wasley)