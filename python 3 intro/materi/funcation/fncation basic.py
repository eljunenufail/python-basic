print("-------------fUNCATIN BASIC---------------")
#funcation diawali dengan kyboard ' def '
def hello_ngab():
    print("halo bang")#wajib ada spce 1 kali untuk menjalan kan print tersebut
    print("halo juga ngab")
    print("-------------------")

def sapa_sapa(nama):
    print("halo kak", nama)
    print("iyaa salken", nama)
    print("-------------------")

def luas_persegi_panjang(panjang, lebar):
    print(">panjang:", panjang)
    print(">lebar:", lebar)
    rumus = panjang * lebar
    print("luas persegi panjang =", rumus)
    print("_____________________________")

def luas_belah_ketupat(luas, diagonal1, diagonal2):
  print(">diagonal1 ->",diagonal1)
  print(">diagonal2 ->", diagonal2)
  rumus = 0.5 * diagonal1 * diagonal2
  print("luas belah ketupat =", rumus)
  print("_____________________________")
  
hello_ngab()
hello_ngab()
hello_ngab()
sapa_sapa("dhian")
sapa_sapa("dhian")
luas_persegi_panjang(20, 2000)
luas_belah_ketupat(0.5, 8, 20)
