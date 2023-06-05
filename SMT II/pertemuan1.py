"""
STRING
"""

nama = "Michael Valensio One Febian"
nim = 5220411200
kelas = "D"
hobi = "tidur"
noHp = "+62822-5340-0079"
email = "michaelfebian353@gmail.com"

# beberapa metode print
print("Nama saya :",nama)
print("Nama saya :"+nama)
print("Nama saya :{}".format(nama))
print("Nama saya : %s"%(nama))

# menjadi kecil
print(nama.lower())

# kapital
print(nama.upper())

# replace
print(nama.replace("Febian","Febiantoo"))

# mencari panjang value
print(len(nama))

# mencari awalan
if noHp[0] == '+' and noHp[1] == '6' and noHp[2] =='2' :
    print('Ini merupakan nomor dari Negara Indonesia')

if noHp.startswith("+62"):
    print("No ini dari indonesia")
# contoh penerapan filter data menggunakan startswith
# seumpama kita memiliki data data no hp yang banyak dan ingin mem-filter data tersebut berdasarkan 
# asal negara nya
print("filter data email")
noHp = ["+6282234576898", "+607363519283", "+631928373839", "+46789654235", 
        "+6284356732617", "+601837417324", "+633746573839", "+46123578898",
        "+6289876540987", "+601826394000", "+630393894059", "+46909807654",
        "+6280087648574", "+603747598338", "+637364591019", "+46125896530"]
# filter data 
noHP_indonesia = [x for x in noHp if x.startswith("+62")]
noHP_malaysia = [x for x in noHp if x.startswith("+60")]
noHP_filipin = [x for x in noHp if x.startswith("+63")]
noHP_swedia = [x for x in noHp if x.startswith("+46")]
# menampilkan data no hp indo
print("="*40)
print("Data no hp Indonesia :")
for i in noHP_indonesia:
    print(noHP_indonesia.index(i) +1, end=' ')
    print(" ",i)
print("="*40)
# menampilkan data no hp malaysia
print("Data no hp Malaysia :")
for i in noHP_malaysia:
    print(noHP_malaysia.index(i) +1, end=' ')
    print(" ",i)
print("="*40)
# menampilkan data no hp filipin
print("Data no hp Filipina :")
for i in noHP_filipin:
    print(noHP_filipin.index(i) +1, end=' ')
    print(" ",i)
print("="*40)
# menampilkan data no hp sweden
print("Data no hp Swedia :")
for i in noHP_swedia:
    print(noHP_swedia.index(i) +1, end=' ')
    print(" ",i)
print("="*40)

# mencari akhiran
if email.endswith("gmail.com"):
    print("Ini dari gmail")
# contoh penerapan filter data menggunakan endswith
# seumpama kita memiliki data data email yang banyak dan ingin mem-filter data tersebut berdasarkan 
# jenis email nya
print("filter data email")
email = ["michaelfebian353@gmail.com", "valenfebian@yahoo.com", "anakuty@outlook.com", "michael.5220411200@student.uty.ac.id", 
        "cahhjogjaaaa12345@gmail.com", "hezranarkee@yahoo.com", "melkysinun@outlook.com", "hezran.5220411215@student.uty.ac.id",
        "rossipratama242@gmail.com", "sinungantengpol@yahoo.com", "dioncinasipit@outlook.com", "dionisius.5220411195@student.uty.ac.id",
        "chiggajayajaya12@gmail.com", "niasxcina@yahoo.com", "akutheo@outlook.com", "theodorus.5220411202@student.uty.ac.id"]
# filter data 
data_gmail = [x for x in email if x.endswith("gmail.com")]
data_yahoo = [x for x in email if x.endswith("yahoo.com")]
data_outlook = [x for x in email if x.endswith("outlook.com")]
data_student = [x for x in email if x.endswith("student.uty.ac.id")]
# menampilkan data gmail
print("="*40)
print("Data akun dari Gmail :")
for i in data_gmail:
    print(data_gmail.index(i) +1, end=' ')
    print(" ",i)
print("="*40)
# menampilkan data yahoo
print("Data akun dari Yahoo :")
for i in data_yahoo:
    print(data_yahoo.index(i) +1, end=' ')
    print(" ",i)
print("="*40)
# menampilkan data outlook
print("Data akun dari Outlook :")
for i in data_outlook:
    print(data_outlook.index(i) +1, end=' ')
    print(" ",i)
print("="*40)
# menampilkan data outlook
print("Data akun Email student :")
for i in data_student:
    print(data_student.index(i) +1, end=' ')
    print(" ",i)
print("="*40)

    



# memecah kalimat menjadi kata
kalimat = "saya sedang makan"
print(kalimat.split())

# menggunakan separator "#"
kalimat = "ayah#sedang#makan#siang#dikantor"
print(kalimat.split("#"))

# menggunakan split dengan dua parameter (separator dan maxsplit)
# maka hanya ada 3 kata yang di pecah
kalimat = "ayah#sedang#makan#siang#dikantor"
print(kalimat.split("#", 3))

# memastikan untuk menghapus spasi di awal dan di akhir
kata = "valen "
print(kata.strip())