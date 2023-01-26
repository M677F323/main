""" def total(galleons,sickels,knuts):
    return(galleons*17+sickels)*29+knuts

print(total(100,50,25)) """

""" def total(galleons,sickels,knuts):
    return(galleons*17+sickels)*29+knuts

coins=[100,50,25]
print(total(coins[0],coins[1],coins[2]))  """

def total(galleons,sickels,knuts):
    return(galleons*17+sickels)*29+knuts

coins = {"galleons":100,"sickels":50,"knuts":25}
#print(total(coins["galleons"],coins["sickles"],coins["knuts"]))
print(total(**coins))

#unpacking **************
#coins=[100,50,25]
#print(total(*coins))
#print(total(galleons =100,sickels = 50 ,knuts = 25))