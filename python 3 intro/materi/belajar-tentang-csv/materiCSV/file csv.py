import csv

file_path = r"C:\Users\SPC LIFE 5\Documents\CODING PYTHON'\python 3 intro\materi\belajar-tentang-csv\materiCSV\data.csv"
with open(file_path, "r") as file_baru:
	next(file_baru)
	read = csv.reader(file_baru)
	list_read = list(read)
	#print(f"isi data{list_read}")
	#file_baru.close()
	

# di eksekusi dengan lebih rapih dengan memakai ( for loop)
print("isi semua data")
print("-" * 20)
for baris in list_read:
	no = baris[0]
	nama = baris[1]
	kelas = baris[2]
	print(f"{no} | {nama} | {kelas}")

# 2. menambahkan dengan data baru
data_baru=[4,"faiz",9]
#open () -> mebuka filr dari file path
#mode 'a' -> append (tambah data)
#newline-> tamabh baris baru dengan teks kosong
#with ....as ->buka file dengan tutup otomatis

with open(file_path,"a",newline="") as file_pesan:
 #aktifkan mode writer csv dari file target
 writer= csv.writer(file_pesan)
 #tambahkan baris dari wariable jajan baru
 writer.writerow(data_baru)# ( dia akan menambahkan baris baru di (jajan.csv) nya)

