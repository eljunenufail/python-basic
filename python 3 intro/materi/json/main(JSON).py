import json
# tambahkan module 'json' dengan import
print("MATERI 12 - JSON FILE HANDLING")
print("---------read JSON------------")
file_path_json = r"C:\Users\ahmad\Documents\coding\JSON.PY\json materi.json"
with open(file_path_json, "r") as file_materi:# with open biar di akhir nggak tulis (close) lagi jadi dia sudah otomatis
	# 1. json.load()-> membaca isi file json
	data_materi = json.load(file_materi)
    # akses data json dengan 'key' nya
	print(f"judul berkas: {data_materi['title']}")
	print(f"judul berkas: {data_materi['total']}")
	print(f"judul berkas: {data_materi['status_santri']}")
	print(f"judul berkas: {data_materi['status_lulus']}")
	print(f"judul berkas: {data_materi['materi_pelajaran']}")
	#extrak data list dengan for loop
for pelajaran in data_materi["materi_pelajaran"]:
	print(f"->>: {pelajaran}")

# ekstrak semua data arrayof object surah
# di python diebut jga dictionary

#1. keys surah : no, nama, ayat, turun.
print("-" * 50)# bisa di gandakan agar lebih shorcut ngetik ny hehehe:v
print("no | nama surah | ayat | turun |")
print("-" * 50)

# extrak data list dengan for loop
for surah in data_materi["surah"]:
    print(f"{surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']} |")
