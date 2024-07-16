import http.client
import json
import pprint
from key import KEY

#for position
conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.formula-1.api-sports.io",
    'x-rapidapi-key': KEY
    }

conn.request("GET", "/rankings/races?race=1", headers=headers)

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




#for location 
conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.formula-1.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/races?competition=1&season=2019", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



