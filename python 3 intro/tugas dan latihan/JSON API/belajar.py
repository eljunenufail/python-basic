import requests

# Endpoint API
url_arab = "https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
url_inggris = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"

# Ambil teks Arab
resp_bahasa_arab = requests.get(url_arab).json()
ayat_arab = resp_bahasa_arab["data"]["text"]

# Ambil teks Inggris (Asad)
resp_inggris = requests.get(url_inggris).json()
ayat_inggris = resp_inggris["data"]["text"]

# Cetak hasil
print("Ayat Al-Kursi (2:255) Arab:")
print(ayat_arab)
print("\nTerjemah (EN):")
print(ayat_inggris)
