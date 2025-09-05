#set = {} = tidak berurutan, berubah, tidak duplikat
game_azka = {"valorant", "delta", "roblox"}
game_syahid = {"minecraft", "roblox", "point blank"}
game_azka.add('minecraft')
game_syahid.add('COD')
game_azka.remove('valorant')

print("game azka:", game_azka)
print("game syahid:", game_syahid)
game_gabungan = game_azka & game_syahid # & = atau/or
print("daftar game ke2nya:", game_gabungan)
#for (loop) untuk mengeluarkan item 1 per 1 dri set
for game in game_gabungan:
    print(game)
    print("---> transfer data game" ,game, "ke play game terpilih")

