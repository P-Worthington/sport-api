import http.client
import json
import pprint
from key import KEY

#race=1 is 2014 australian gp
#for position
conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.formula-1.api-sports.io",
    'x-rapidapi-key': KEY
    }

conn.request("GET", "/rankings/races?race=800", headers=headers)

res = conn.getresponse()
data = res.read()

decoded = data.decode("utf-8")

dictData = json.loads(decoded)

winner = dictData["response"][0]
del winner["gap"]

pprint.pprint(winner)

second = dictData["response"][1]
del second["gap"]
pprint.pprint(second)



#2014 australia gp
#for location 
conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.formula-1.api-sports.io",
    'x-rapidapi-key': KEY
    }

conn.request("GET", "/races?competition=1&season=2024", headers=headers)

res = conn.getresponse()
data = res.read()

#pprint.pprint(data.decode("utf-8"))



