#API Application programming interface connection b/w code and userinterface  
#it use web browser and also download thirdparty sites

#Requests it is most important library in the these API

import requests
import json
import sys

if len(sys.argv) < 2:
    sys.exit("too few")
#its like downloading and assigning it to respons add adding argument vector #10
response =requests.get("https://itunes.apple.com/search?entity=song&limit=10000&term="+sys.argv[1])
#json() to give output as json
print(response.json())
#json.dumps to decorate with indent 2
#print(json.dumps(response.json(), indent = 2 ))
o = (response.json())
# in results we have trackName
for arg in o["results"]:
    print(arg["trackName"])
