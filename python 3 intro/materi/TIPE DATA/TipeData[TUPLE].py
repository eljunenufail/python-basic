print('-------------TUPLE------------------')
# tuple  (berurutan, tidak bisa diubah, dan boleh duplikat)
# penulisan nya menggunakan ()

# contoh [no_index] akses dta tuple
ttl =(10, "juli", 2010)# tuple tidak bisa diubah
print("tanggal lahir juna", ttl)
print("tanggal:",ttl[0])
print("bulan:",ttl[1])
print("tahun:",ttl[2])
# akss pada tulisan BULAN pada [posisi index dia yang asli] : lalu index batas terakhir item itu yang bukan di hitung dari 0
print("bulan tahun:",ttl[1:3])# ini akan mengakses index 1 sampai 2 dalam hituangan dari agka 0
# mengkuti urutan item nya
# unpacking tuple ke variable baru
tanggal, bulan, tahun = ttl
print(tanggal)
print(bulan)
print(tahun)
#cara lain
tanggal_lahir,bulan_lahir,tahun_lahir=ttl
print(tanggal_lahir)
print(bulan_lahir)
print(tahun_lahir)
#manipulai list lanjutan
#menggabungkan dengan tuple lain
jajanMasboy = ("keripik", "cokelat")
jajanSyahid = ("kelapa", "pisang")
jajanan_mereka = (jajanMasboy + jajanSyahid) #menggabungkan tuple
print("jajanan mereka:", jajanan_mereka)

#list multi dimensi (list di dalam nya ad list)
list_minuman = [
    ["teh", "kopi", "susu"], #index 0
    ["jeruk", "mangga", "apel"], #index 1
    ["air putih", "es teh", "es jeruk"] #index 2
    ]
print("sedia minuman:", list_minuman)
print(list_minuman[1] [2])