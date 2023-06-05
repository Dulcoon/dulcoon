# NPM : 5220411200
# Nama : Michael Valensio One Febian


# "Menghitung Luas Bangun Di Module
print("Menghitung Luas Bangun Persegi Panjang")
P=float(input("Masukan Panjang dari persegi panjang ="))
L=float(input("Masukan Lebar dari persegi panjang ="))
Luas_persegi_panjang=(P*L)
print("Luas Persegi Panjang adalah",Luas_persegi_panjang, "cm2")

print("Menghitung Luas Bangun setengah lingkaran")
phi=22/7
R=float(input("Masukan jari-jari lingkaran ="))
Luas_setengah_lingkaran=float(0.5*phi*R*R)
print("Luas setengah lingkaran adalah",Luas_setengah_lingkaran, "cm2")

print("Menghitung Total Luas Kedua Bangun")
Luas_kedua_bangun=(Luas_persegi_panjang + Luas_setengah_lingkaran)
print("Total luas kedua bangun adalah",Luas_kedua_bangun, "cm2")

