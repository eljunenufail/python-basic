# list [] (brurutan, bisa diubah, dan boleh duplikat)

print("-----DAFTAR BELANJA DALAM KERANJANG------")

daftar_belanja = ["teh desa", #index 0
                  "gabin", #index 1
                  "pisang kembung", #index 2
                  "naspad kawan lamo" #index 3
]  
# mengakses list lewat index         
print("isi belanjaan kamu", daftar_belanja)
print("belanjaan pertama:", daftar_belanja[0])
print("belanjaan kedua:", daftar_belanja[1])
print("belanjaan ketiga:", daftar_belanja[2])
print("belanjaan keempat:", daftar_belanja[3])
#menambah item baru ke akhir list
daftar_belanja.append("olive chiken")
daftar_belanja.append("ayam geprek")
print("isi belanjaan kamu sekarang;", daftar_belanja)
print("belanjaan kelima:", daftar_belanja[4])
# menghapus item dari list
daftar_belanja.remove("gabin")
print("isi belanjaan kamu terakhir:", daftar_belanja)
print("----DAFTAR BELANJAAN KAMU SUDAH SELESAI------")