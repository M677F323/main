#API Application programming interface connection b/w code and userinterface  
#it use web browser and also download thirdparty sites

#Requests it is most important library in the these API

import requests
import json
import sys

if len(sys.argv) < 2:
    sys.exit("too few")
#its like downloading and assigning it to respons add adding argument vector
response =requests.get("https://itunes.apple.com/search?entity=song&limit=2&term="+sys.argv[1])
#json() to give output as json
print(response.json())
#json.dumps to decorate
o = (response.json())
for arg in o["results"]:
    print(arg["trackName"])
n