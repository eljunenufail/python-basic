import csv
file_path = r"C:\Users\SPC LIFE 5\Documents\CODING PYTHON'\TUGAS 3\keuangan.csv"
with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

print("Tanggal | Keterangan | Kategori | Jumlah")
print("-" * 50)
for baris in list_read:
    tgl = baris[0]
    ket = baris[1]
    kategori = baris[2]
    jumlah = baris[3]
    print(f"{tgl} | {ket} | {kategori} | {jumlah}")


  