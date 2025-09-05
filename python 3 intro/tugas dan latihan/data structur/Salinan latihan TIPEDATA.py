# no 1 dengan lIST
print("------------DAFTAR UJIAN SEKOLAH--------------")

jadwal_ujian = ["senin : fiqih", "selas. : tajwid", "rabu. : MTK,", "kamis. : b.indo", "jum'at. : b. arab"]
print("DAFTAR UJIAN SEKOLAH")
for jadwal in jadwal_ujian:
    print(jadwal)

# atau biasa juga dengan

#for item in jadwal_ujian:
    #print(f"-{item}")
print("-------------selsai tantangan 1-------------------")

# no 2 dengan TUPPLE
print("-------------rukun islam-----------------")
rukun_islam = ('syahadat', 'shalat', 'zakat', 'puasa', 'haji')

print("RUKUN ISLAM")

for i in range (len(rukun_islam)):
    print(f"{ i + 1}-> {rukun_islam[i]}")
print("--------------selesai tantangan 2---------------------")

# no 3 dengan SET
print("--------------------nama kitab-------------------------")
nama_kitab = {"usulusstalsah", "matan abi syuja", "tajwid almushawwir", "kitaabuttauhid"}
print("NAMA NAMA KITAB YANG DI PELAJARI")
for kitab in nama_kitab:
    print("--->" ,kitab)
print("--------------selesai tantangan 3---------------------")

print("-------------BIODATA KAMU-----------------")
#no 4 dengan DICTIONARY
juna = {
    "nama" : "juna",
    "umur" : 15,
    "asal" : "bekasi",
    "kelas" : "x.a"
}
print("BIODATA KAMU")
for key, value in juna.items():
    print(f"{key} -> {value}")
print("--------------selesai tantangan 4---------------------")

