# array list tuple
# Nama : Michael valensio One Febian
# NIM  : 5220411200
# IF D


from array import *
Angka=[11,12,13,14,15,16,17,18,19,20]
x=len(Angka)
print(Angka)
for i in range (x):
    print("data ke",i,"  ",Angka[i])
for y in Angka:
    print(y, end=" ")
    
# update data
print("Update nilai di list")
i=int(input("Ubah data ke berapa? "))
print("Data ke ",i,"Adalah",Angka[i])
Angka[i]=int(input("Masukkan data yamh baru : "))
print(Angka)

# delete data
print("Menghapus data di list")
i=int(input("Hapus data ke berapa? "))
print("Data ke ",i,"Adalah",Angka[i])
del Angka[i]
print("Data sudah dihapus")
print(Angka)

# data terbesar dan terkecil
print("Data terbesar dalam list adalah", max(Angka))
print("Data terkecil dalam list adalah", min(Angka))

# mengurutkan data di list
Angka.sort()
print(Angka)
print("jUMLAH Anggota list",len(Angka))

# slicing
print("Ini Slicing")
print(Angka[1])
print(Angka[:3])
print(Angka[:])
print(Angka[::-1])
print(Angka[::-2])
print(Angka[::-3])
print(Angka[::2])