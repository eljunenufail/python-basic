import json
file_path = r"C:\Users\SPC LIFE 5\Documents\CODING PYTHON'\git\python 3 intro\tugas dan latihan\JSON API\peminjaman_buku.json"
with open(file_path, 'r') as file:
    data = json.load(file)
    
total_dipinjam = 0
total_belum_kembali = 0

print("Belum kembali:")
for anggota in data["anggota"]:
    for buku in anggota["pinjam"]:
        total_dipinjam += 1
        if not buku["kembali"]:
            total_belum_kembali += 1
            print(f"- {anggota['nama']} : {buku['judul']} ({buku['tanggal']})")
print("data semua buku yang di pinjam:")
print(f"Total dipinjam: {total_dipinjam}")
print(f"Belum kembali: {total_belum_kembali}")
