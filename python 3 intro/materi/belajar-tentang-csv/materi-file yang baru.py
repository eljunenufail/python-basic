import csv

#tambahkan module 'csv' dngan 'import'
print ("-----------materi 11 file heanding part 2---------------") 
#baca isi file -> extrak data -> buat data baru
#-> baut / tulis ulang semua baris nya dengan mode 'w'
file_path_csv = r"C:\Users\SPC LIFE 5\Documents\CODING PYTHON'\python 3 intro\materi\belajar-tentang-csv\jajan.csv"
# siapkan data jajan kosong []
# untuk menampung data dari csv ke list
data_jajan = []
   
with open(file_path_csv, "r") as isi_jajan:
    # csv.reader() -> membaca isi file csv 
    reader = csv.reader(isi_jajan)
    # extrak semua data dengan for loop
    for item_jajan in reader:
        print(item_jajan)
        # tambah item ke list data jajanan
        data_jajan.append(item_jajan)


