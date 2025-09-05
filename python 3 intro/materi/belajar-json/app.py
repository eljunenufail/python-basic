import requests
kota = input("masukkan nama kota :")
url = f"https://api.aladhan.com/v1/timingsByCity/30-08-2025?city=Jakarta&country=Indonesia&method=20"
response = requests.get(url) # Http Get (ambil data)
data_json = response.json()
print(f"Jadwal Sholat {kota}")
print("-" * 40)
#print data json
#akses data sholat berdasarkan hirarki keys yang ada
#-> data-> timings -> keynamasolatnya
jadwal_sholat = data_json['data']['timings']#versi ringkas di potong
print(f"-> shubuh = {jadwal_sholat['Fajr']}")
print(f"-> sunrise = {jadwal_sholat['Sunrise']}")
print(f"-> Maghrib = {data_json['data']['timings']['Maghrib']}")
