# # DICTIONRY (dict) = {key:value} / {kunci:nilai}
# # berurutan, berubah, tidak duplikat

# kamus_anime ={
# "blue_lock":"isage ren",
# "demon_slayer":"tanjiro",
# "waifu":{
#     "one_piece":"nami",
#     "naruto":"tsunade",
#          }
# }
# print("kamus anime:", kamus_anime)
# print("MC blue lock:", kamus_anime["blue_lock"])
# print("MC demon slayer:",kamus_anime["demon_slayer"])
# print("WAIFU one piece:", kamus_anime["waifu"]["one_piece"])

# #nambah item baru ke dictionary
# kamus_anime["naruto"]="shikamaru"
# print("MC naruto:", kamus_anime["naruto"])

# #mengubah item dari dictionary
# kamus_anime["demon_slayer"] = "zinetsu"

# # mengahapus item dari dictionary
# del(kamus_anime['blue_lock'])
# print("kamus anime terbaru:", kamus_anime)







# Latihan dasar
# dictionary
Juna = {
    "umur": 15,
    "asal": "bekasi",
    "kelas": "10 a"
}
# Operasi pada dictioary

# 1. mengakses nilai nya!!!!
print(Juna["asal"])

# 2. menambahkan nilai di dictionary
Juna["berat badan"] = 55
print(Juna)
Juna["hobi"] = "main futsal"


# 3. mengubah nilai di dictionary
Juna["berat badan"] = 60
print(Juna)

# 4. menghapus nilai
del(Juna["kelas"])
print(Juna)

# 5. mengecek key nya
print("asal" in Juna) #dia seperti menanyakan yang ada di tanda kutip trsbt, apkah ada pada list Juna

# 6. Mendaptkan semua key dan velue nya
print(Juna.keys())

# 7. mengecek value nya apa aja
print(Juna.values())


# 8. ---------------------LOOPING-----------------------------------#

# memasang key nya saja

for key in Juna:# otomatis dia memang hanya mengambil data key nya saja!! tanpa memakai kode lain seperti (.keys() )
    print(key)
print("akhir dari pemograman dict loop memakai key nya")

# memasang value nya saja

for value in Juna.values():# cara mengambil value nya SAJA memakai(.values() ) dia akhir lis tersebut
    print(value)
print("akhir dari pemograman dict loop memakai value nya")

# memasang kedua k:v dalaam bersamaan

for key, value in Juna.items():# jika ingin memasukan key nya dan value nya bersamaaan maka di akhir list nama nya memakai (.items() )
    print(f"{key} -> {value}")# f kegunaaan nya untuk memasukin variable agr bisa di print
print("akhir dari pemograman dict loop memakai key dan value nya bersamaan")



#  Nasted dictionary

kelas = {
    "siwa1": {
        "nama":"juna",
        "kelas":"x.a",
        "asal":"bekasi",
        "hobi": {
            "hobi1":"makan",
            "hobi2":"turu",
            "hobi3":"marah marah",
        
            
            
        },
    },
}

print(kelas["siwa1"]["hobi"])