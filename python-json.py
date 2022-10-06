import json
# membuka file json
file_json = open("biodata.json")
# parsing data json
data = json.loads(file_json.read())
# cetak data json
print(f"Nama: {data['nama']}")
print(f"Agama: {data['agama']}")
print(f"Hobi: {data['hobi']}")
print(f"Negara: {data['negara']}")
# print(data)