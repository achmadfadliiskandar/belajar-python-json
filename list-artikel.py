import json
from urllib import request

url = "https://jsonplaceholder.typicode.com/posts"

response = request.urlopen(url)

data = json.loads(response.read())

for i in data:
    print(f"{i['id']}.{i['title']}")