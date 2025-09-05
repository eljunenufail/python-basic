print("===== PROFIL DIGITAL KAMU =====")
nama = input("nama?")
umur = input("umur?")
kelas = input("kelas?")
hobi = input("hobi?")
cita2 = input("cita-cita?")
waktuBelajar = input("waku terenak buat belajar?")
tanggalLahir = input("tanggal lahir?")


print("===== PROFIL DIGITAL KAMU =====")

(print("1.wibu"))
(print("2.gamer"))
(print("3.kpopers"))
(print("4.anak konten"))
(print("5.anak nongki"))
 
tipe = int(input("kamu tipe apa? (1-5): "))

if tipe == 1:
    print("pasti kamu sering maraton anime sampai malam")
    waifu = input("siapa waifu kamu")
    print(waifu, "sangat cantik")
    print("wah Anak anime banget")


elif tipe == 2:
    print("rank jalan terus")
    game = input("Game favorit kamu apa?")
    if game == "mobile legends":
     print("main terus sampai rank mythic")
    if game == "ff":  
     print("main terus sampai rank grandmaster")
    
elif tipe == 3:
    print("Ngikutin gaya Korea")
    idol  = input("siapa bias kamu")
    if "kpopers" == "idol":
     print("idol kamu keren")

elif tipe == 4:
    print("Tiktoker/Youtuber")
    konten = input("platfrom favorit kamu apa?")
    if konten == "tiktok":
        print("tiktokers sejati")
    if konten == "youtube":
        print ("youtuber sejati")

elif tipe == 5:
    print("Yang penting ngumpul")
    nongki = input("Nongkrong paling sering di mana?")
    if nongki == "kafe":
        print("Kafe buat kencan itu bagus")
    if nongki == "warung kopi":
        print("Warung kopi buat mabar bareng asik banget")
    if nongki == "restoran":
        print("Restoran tempat makan bareng keluarga lebih nyaman")
    else:
        print("Nongkrong di tempat lain juga asik")

print("---------------FUN CHECK-----------------")


pertanyaan = input ("teman sebelahmu bau badan?")
if pertanyaan == "iya":
        print("suruh mandi aja bang sekalian")
else:
       print("kamu beruntung banget dapet jackpot punya temen kayak dia")