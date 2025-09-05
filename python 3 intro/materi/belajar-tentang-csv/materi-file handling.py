# buka file
import csv


file_path = r"C:\Users\SPC LIFE 5\Documents\CODING PYTHON'\python 3 intro\materi\belajar-tentang-csv\pesan.txt"
#buka file nya
file_pesan = open(file_path, "r")
#baca isi file
isi_pesan = file_pesan.read()
#tampilkan isi output pesan nya
print(f"ISI PESAN KABAR => {isi_pesan}")
#tutup file
file_pesan.close()


print("------------data CSV-------------------")
print("__MATERI 10__")
print("===================")
file_path=r"C:\Users\SPC LIFE 5\Documents\CODING PYTHON'\python 3 intro\materi\belajar-tentang-csv\jajan.csv"
#buka file
file_pesan=open(file_path,"r")
#baca isi file
isi_pesan=file_pesan.read()
#tampilkan output isi pesan
print(f"ISI PESAN => {isi_pesan}")
#tutup pesan
file_pesan.close()

print("-----APPEND CSV FILE------")

jajan_baru=[6,"sabtu",10000]
print(f"jajan baru:{jajan_baru}")
#open () -> mebuka filr dari file path
#mode 'a' -> append (tambah data)
#newline-> tamabh baris baru dengan teks kosong
#with ....as ->buka file dengan tutup otomatis

with open(file_path,"a",newline="") as file_pesan:
 #aktifkan mode writer csv dari file target
 writer= csv.writer(file_pesan)
 #tambahkan baris dari wariable jajan baru
 writer.writerow(jajan_baru)# ( dia akan menambahkan baris baru di (jajan.csv) nya)
  
  

