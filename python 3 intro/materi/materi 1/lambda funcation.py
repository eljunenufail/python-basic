print("-------------------LAMBDA FUNCTION-------------------------")
print("-----------------------------------------------------------")
# funcation tidak akan bsa di ekesekusi apabila tidak di panggil
def say_hello(name):
# kasih "f" di awal print  string untuk menyisipkan variable/paramater
# dengan diapil {nama_variable}
    print(f"halo sayang. {name}")
    print("haiiii juga")

# lambda untuk menulis fungsi yang ringkas dengan 1 baris saja
# sering juga di sebut anonim (tapa nama)
say_hello_mini = lambda name: print(f"hello aa. {name}")
# panggil fungsi2 nya di bawah iini
say_hello("juna")
say_hello_mini("juna")
print("---------------------------------------------------------->")


# contoh penerapan lomda higher order funcation
# 1.map(), 2.sorted() 3.filter()

#sorted -> mengurutkan data
jajan_mingguan = [12000, 5000, 10000, 20000, 100000]
urutkan_uang = sorted(jajan_mingguan)
urutkan_uang_terbalik = sorted(jajan_mingguan, reverse=True)
print(f"uratkan uang. {urutkan_uang}")
print(f"urutkan uang terbalik. {urutkan_uang_terbalik}")

# map mentransormasi data
kurangin_uang = map(lambda uang : uang - 5000, jajan_mingguan)

#list() mengubah data objek map menjadi list
list_kurangin_uang = list(kurangin_uang)
print(f"map uang berkurng: {list_kurangin_uang}")

# filter() menyaring/ memfilter data
jajan_banyak = filter(lambda uang : uang >= 100000, jajan_mingguan) 
list_jajan_banyak = list(jajan_banyak)
print(f"jajan terlalu banyak 100.000: {list_jajan_banyak}")
