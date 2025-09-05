print ("python bginner - materi 1")
# for looping (index di mulai dari 0 sampai 5)
for angka in range(0, 5):
    print("halo ke-", angka)

for player in range(0, 10):
   print("halo player-", player)
print("kelazz king")
print("-----THE END-----")#print nya harus dipojok yang kedua dan tiga biar selesai nya di akhir

# for loop ke string
sandiWifi = "copet"
for huruf in sandiWifi:
    print(huruf,"==>")

# 1.while loop (ulangi sampai kondisi terpenuhi)
no = 1
batas = 20
while (no < batas):
    print("ulangi ke-", no)
    no += 1
# 2.while loop (ulangi sampai kondisi terpenuhi)
no = 1
batas = 20
while (no < batas):
    print("*" * no)
    no += 1

# LATIHAN SENDIRI
# ini dengan list

angka2 = (0, 1, 2, 3, 4, 5) 
for i in angka2:
    print(f"i adalah {i}")

#latihan pake nama

for i in range(10):
    print("zidan bau eek")
print("akhir dari perogram looping nama")

#looping angka

angka2_range = range(0, 10)
for i in angka2_range:
    print("saya keren")       
print("akhir dari perogram looping angka") 

#looping huruf yang 1 lis / item

data_str = "juna ganteng banget" #kalau hanya 1 list atau item dia bakalan ngeprint  satu persatu huruf nya
for huruf in data_str:
    print(huruf) 
print("akhir dari program looping huruf")

   #looping nama hari
     
nama_hari= ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
for hari in nama_hari:    
 print(hari)
print("akhir dari pemograman dari loping nama hari")

# looping angka genap
 
angkaGanjil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in angkaGanjil:
    if i % 2 ==1:
        print(i)

nama = "koyok eek"
for huruf in nama:
    print(nama, "itulah zidan")