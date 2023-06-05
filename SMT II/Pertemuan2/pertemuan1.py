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
print("Nama saya :{}".format(nama))
print("Nama saya : %s"%(nama))

# menjadi kecil
print(nama.lower())

# kapital
print(nama.upper())

# replace
print(nama.replace("Febian","Febbbbb"))

# mencari panjang value
print(len(nama))

# mencari awalan
if noHp[0] == '+' and noHp[1] == '6' and noHp[2] =='2' :
    print('Ini merupakan nomor dari Negara Indonesia')

if noHp.startswith("+62"):
    print("No ini dari indonesia")
    
# mencari akhiran
if email.endswith("gmail.com"):
    print("Ini dari gmail")
    
# memecah kalimat menajdi kata
kalimat = "saya sedang makan"
print(kalimat.split())

# memastikan untuk menghapus spasi di awal dan di akhir
kata = "valen "
print(kata.strip())