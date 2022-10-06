import json
from urllib import request

url = "https://www.bwfshuttleapi.com/rankings/api/MS"
response = request.urlopen(url)
data = json.loads(response.read())
for badminton in data:
    print(f"{badminton['rank']} {badminton['player']} {badminton['country']}")