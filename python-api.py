import json #module
from urllib import request # library dari urlib di import jadi request
# url nya
url = "https://api.github.com/users/achmadfadliiskandar"
# permintaan membuka api dari github
response = request.urlopen(url)
# membaca/parse / merespon permintaan dari variabel response
data = json.loads(response.read())
# mencetak inputan
print("==Baca Profile Lengkap Github==")
print(f"Nama: {data['name']}")
print(f"Lokasi: {data['location']}")
print(f"Nomor Identitas: {data['id']}")
print(f"Keterangan: {data['bio']}")
print(f"Pengikut: {data['followers']} orang")
print(f"Yang Diikuti: {data['following']} orang")