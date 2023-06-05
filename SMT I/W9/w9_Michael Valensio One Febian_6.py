buku=dict(
    judul= "Algoritma Pemrograman",
    penulis= "Insap santoso",
    harga= 75000
)

# mencetak dengan looping
# for key in buku:
#     print(key, "->", buku[key])
    
# looping2
# for nama_attr,nama in buku.items():
#     print(nama_attr, "->",nama)

# cetak
# print("=========================================")
# print("judul Buku",buku.get("judul"))
# print("Penulis Buku",buku.get("penulis"))
# print("Harga Buku",buku.get("harga"))
# print("=========================================")

# # edut data dict
# a=str(input("Masukkan Penulis Yang baru : "))
# buku["penulis"]=a
# print("=========================================")
# print("judul Buku",buku.get("judul"))
# print("Penulis Buku",buku.get("penulis"))
# print("Harga Buku",buku.get("harga"))
# print("=========================================")

# # mengubah item baru
# b = int(input("Maukkan Jumlah halaman buku : "))
# buku["jumhal"]=b
# print("=========================================")
# print("judul Buku",buku.get("judul"))
# print("Penulis Buku",buku.get("penulis"))
# print("Harga Buku",buku.get("harga"))
# print("Jumlah Halaman",buku.get("jumhal"))
# print("=========================================")
# buku.clear()
# print("=========================================")
# print("judul Buku",buku.get("judul"))
# print("Penulis Buku",buku.get("penulis"))
# print("Harga Buku",buku.get("harga"))
# print("Jumlah Halaman",buku.get("jumhal"))
# print("=========================================")



# # mengubah item baru
a = str(input("Masukkan Penulis baru : "))
buku["penulis"]=a
b = int(input("Maukkan Jumlah halaman buku : "))
buku["Jumlah_Halaman"]=b
c = str(input("Masukkan Warna Buku : "))
buku["Warna_Buku"]=c
buku.clear
# mencetak dengan looping
for key in buku:
    print(key, "->", buku[key])